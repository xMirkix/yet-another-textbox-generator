from __future__ import annotations
from dataclasses import dataclass
import re
from typing import Callable

from bs4 import BeautifulSoup

from running.connection.importing.import_cache import RequestCache

FONT_FALLBACKS = {
    "earthbound": "determination mono",
}

TRANSFORM_ID_BY_PHRASE = {
    "without changes in capitalization": 1,
    "in uppercase": 2,
    "in lowercase": 3,
    "Capitalizing Every Word": 4,
}

FONT_TRANSFORM_PATTERN = re.compile(
    r"Uses the (?P<font>.+?) font and speaks (?P<transform_phrase>.+?)\.",
    re.IGNORECASE
)

ProgressCallback = Callable[[int, int], None]

@dataclass
class ImportedExpression:
    title: str
    image_bytes: bytes


@dataclass
class ImportedCharacter:
    name: str
    font_name: str
    transform_id: int
    expressions: list[ImportedExpression]


def fetch_character(username: str, slug: str, cache: RequestCache, on_progress: ProgressCallback | None = None) -> ImportedCharacter:
    url = f"https://www.demirramon.com/user_content/undertale_character/{username}/{slug}"
    html = cache.get_text(url)
    soup = BeautifulSoup(html, "html.parser")

    name = extract_name(soup)
    font_name, transform_id = extract_font_and_transform(soup)
    expressions = extract_expressions(soup, cache, on_progress)

    return ImportedCharacter(name, font_name, transform_id, expressions)


def extract_name(soup: BeautifulSoup) -> str:
    h1 = soup.find("h1")
    return h1.get_text(strip=True) if h1 else ""


def extract_font_and_transform(soup: BeautifulSoup) -> tuple[str, int]:
    heading = soup.find("h3", string="Textbox")
    if heading is None:
        return "", 1

    paragraph = heading.find_next_sibling("p")
    if paragraph is None:
        return "", 1

    text = paragraph.get_text(" ", strip=True)
    match = FONT_TRANSFORM_PATTERN.search(text)
    if match is None:
        return "", 1

    font_name = resolve_font_name(match.group("font"))
    transform_id = resolve_transform_id(match.group("transform_phrase"))
    return font_name, transform_id


def resolve_font_name(raw_font_name: str) -> str:
    normalized = raw_font_name.strip().lower()
    return FONT_FALLBACKS.get(normalized, normalized)


def resolve_transform_id(raw_phrase: str) -> int:
    normalized = raw_phrase.strip().lower()
    for phrase, transform_id in TRANSFORM_ID_BY_PHRASE.items():
        if phrase in normalized:
            return transform_id
    return 1


def extract_expressions(soup: BeautifulSoup, cache: RequestCache, on_progress: ProgressCallback | None = None) -> list[ImportedExpression]:
    containers = []
    for container in soup.select("div.sprite-container-wrap div.pic"):
        img = container.find("img")
        if img is None or not img.get("src") or img.get("id", "").startswith("overworld_"):
            continue
        containers.append((container.get("title", "").strip(), img["src"]))

    total = len(containers)
    expressions = []

    for index, (title, src) in enumerate(containers, start=1):
        image_bytes = cache.get_bytes(src)
        expressions.append(ImportedExpression(title, image_bytes))
        if on_progress is not None:
            on_progress(index, total)

    return expressions