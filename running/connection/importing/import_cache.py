from __future__ import annotations
import requests

class RequestCache:

    _instance: RequestCache | None = None

    def __init__(self):
        self._session = requests.Session()
        self._session.headers.update({
            "User-Agent": "Mozilla/5.0 (compatible; YetAnotherTextboxGenerator/2.0)"
        })
        self._text_cache: dict[str, str] = {}
        self._binary_cache: dict[str, bytes] = {}

    @classmethod
    def get_instance(cls) -> RequestCache:
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def get_text(self, url: str, timeout: float = 10) -> str:
        if url in self._text_cache:
            return self._text_cache[url]
        response = self._session.get(url, timeout=timeout)
        response.raise_for_status()
        self._text_cache[url] = response.text
        return response.text

    def get_bytes(self, url: str, timeout: float = 10) -> bytes:
        if url in self._binary_cache:
            return self._binary_cache[url]
        response = self._session.get(url, timeout=timeout)
        response.raise_for_status()
        self._binary_cache[url] = response.content
        return response.content

    def clear(self) -> None:
        self._text_cache.clear()
        self._binary_cache.clear()
