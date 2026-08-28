from __future__ import annotations
import threading
import requests


class RequestCache:
    _instance: RequestCache | None = None
    _instance_lock = threading.Lock()

    def __init__(self):
        self._session = requests.Session()
        self._session.headers.update({
            "User-Agent": "Mozilla/5.0 (compatible; YetAnotherTextboxGenerator/2.0)"
        })
        self._text_cache: dict[str, str] = {}
        self._binary_cache: dict[str, bytes] = {}
        self._cache_lock = threading.Lock()

    @classmethod
    def get_instance(cls) -> RequestCache:
        if cls._instance is None:
            with cls._instance_lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance

    def get_text(self, url: str, timeout: float = 10) -> str:
        with self._cache_lock:
            cached = self._text_cache.get(url)
        if cached is not None:
            return cached

        response = self._session.get(url, timeout=timeout)
        response.raise_for_status()

        with self._cache_lock:
            if len(self._text_cache) < 100:
                self._text_cache[url] = response.text
            else:
                self._text_cache.clear()
        return response.text

    def get_bytes(self, url: str, timeout: float = 10) -> bytes:
        with self._cache_lock:
            cached = self._binary_cache.get(url)
        if cached is not None:
            return cached

        response = self._session.get(url, timeout=timeout)
        response.raise_for_status()

        with self._cache_lock:
            if len(self._binary_cache) < 130:
                self._binary_cache[url] = response.content
            else:
                self._binary_cache.clear()
        return response.content

    def clear(self) -> None:
        with self._cache_lock:
            self._text_cache.clear()
            self._binary_cache.clear()
