from __future__ import annotations
from dataclasses import dataclass
import requests
from PySide6.QtCore import QObject, QRunnable, QThreadPool, Signal

from running.connection.importing.import_logic import fetch_character, ImportedCharacter
from running.connection.importing.import_cache import RequestCache

MAX_PARALLEL_DOWNLOADS = 3

JOB_WEIGHT = 100


@dataclass
class ImportJob:
    job_id: int
    username: str
    slug: str
    status: str = "running"   # running | done | failed
    current: int = 0
    total: int = 0
    error: str | None = None


class _FetchSignals(QObject):
    progress = Signal(int, int, int)
    finished = Signal(int, object, object)


class _FetchRunnable(QRunnable):

    def __init__(self, job_id: int, username: str, slug: str, signals: _FetchSignals):
        super().__init__()
        self._job_id = job_id
        self._username = username
        self._slug = slug
        self._signals = signals
        self.setAutoDelete(True)

    def run(self):
        cache = RequestCache.get_instance()
        try:
            def report(current: int, total: int):
                self._signals.progress.emit(self._job_id, current, total)

            character = fetch_character(self._username, self._slug, cache, report)
        except requests.RequestException as e:
            self._signals.finished.emit(self._job_id, None, f"Could not reach the page: {e}")
            return
        except Exception as e:
            self._signals.finished.emit(self._job_id, None, f"Could not read the page: {e}")
            return

        if not character.expressions:
            self._signals.finished.emit(self._job_id, None, "No expressions found on that page")
            return

        self._signals.finished.emit(self._job_id, character, None)


class ImportManager(QObject):

    overall_progress = Signal(int, int)
    job_finished = Signal(int, str, str, object)
    all_finished = Signal(int, list)

    def __init__(self, save_callback, max_parallel_downloads: int = MAX_PARALLEL_DOWNLOADS, parent=None):
        super().__init__(parent)
        self._pool = QThreadPool()
        self._pool.setMaxThreadCount(max(1, max_parallel_downloads))

        self._signals = _FetchSignals()
        self._signals.progress.connect(self._on_progress)
        self._signals.finished.connect(self._on_fetch_finished)

        self._save_callback = save_callback
        self._jobs: dict[int, ImportJob] = {}
        self._universe = None
        self._remaining = 0
        self._successes = 0
        self._errors: list[tuple[str, str, str]] = []

    def start(self, universe, pairs: list[tuple[str, str]]):
        self._universe = universe
        self._remaining = len(pairs)
        self._successes = 0
        self._errors = []
        self._jobs = {
            job_id: ImportJob(job_id, username, slug)
            for job_id, (username, slug) in enumerate(pairs)
        }

        self._emit_overall_progress()

        for job_id, (username, slug) in enumerate(pairs):
            self._pool.start(_FetchRunnable(job_id, username, slug, self._signals))

    def _on_progress(self, job_id: int, current: int, total: int):
        job = self._jobs.get(job_id)
        if job:
            job.current, job.total = current, total
        self._emit_overall_progress()

    def _on_fetch_finished(self, job_id: int, character: ImportedCharacter | None, error: str | None):
        job = self._jobs[job_id]

        if error is not None:
            job.status, job.error = "failed", error
            self._errors.append((job.username, job.slug, error))
        else:
            new_character, save_error = self._save_callback(self._universe, character)
            if save_error is not None:
                job.status, job.error = "failed", save_error
                self._errors.append((job.username, job.slug, save_error))
            else:
                job.status = "done"
                self._successes += 1

        self.job_finished.emit(
            job_id, job.username, job.slug,
            job.error if job.status == "failed" else None
        )

        self._emit_overall_progress()

        self._remaining -= 1
        if self._remaining <= 0:
            self.all_finished.emit(self._successes, self._errors)

    def _emit_overall_progress(self):
        total = len(self._jobs) * JOB_WEIGHT
        value = 0
        for job in self._jobs.values():
            if job.status in ("done", "failed"):
                value += JOB_WEIGHT
            elif job.total:
                value += min(JOB_WEIGHT, int(job.current / job.total * JOB_WEIGHT))
        self.overall_progress.emit(value, total)
