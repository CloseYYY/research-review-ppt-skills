#!/usr/bin/env python3
"""Audit structural properties of a PPTX without external dependencies."""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
}
PLACEHOLDER_PATTERNS = (
    "todo",
    "tbd",
    "lorem ipsum",
    "click to add",
    "单击此处添加",
    "双击此处添加",
)
BACKUP_MARKERS = ("【备用页】", "[Backup]")
TIME_PATTERN = re.compile(r"【建议时长】\s*(\d+(?:\.\d+)?)\s*(?:秒|s|sec)", re.IGNORECASE)


def natural_key(value: str) -> list[object]:
    return [int(part) if part.isdigit() else part for part in re.split(r"(\d+)", value)]


def xml_text(data: bytes) -> str:
    try:
        root = ET.fromstring(data)
    except ET.ParseError:
        return ""
    return "".join(node.text or "" for node in root.findall(".//a:t", NS))


def talk_text(note_text: str) -> str:
    text = note_text.split("[Sources]", 1)[0]
    text = text.replace("【讲稿】", "").replace("【备用页】", "").replace("[Backup]", "")
    return TIME_PATTERN.sub("", text).strip()


def estimate_seconds(note_text: str) -> tuple[int, str]:
    explicit = TIME_PATTERN.search(note_text)
    if explicit:
        return round(float(explicit.group(1))), "explicit"
    text = talk_text(note_text)
    chinese_chars = len(re.findall(r"[\u3400-\u9fff]", text))
    non_chinese = re.sub(r"[\u3400-\u9fff]", " ", text)
    english_words = len(re.findall(r"[A-Za-z0-9]+(?:[-–/][A-Za-z0-9]+)*", non_chinese))
    seconds = chinese_chars / 240 * 60 + english_words / 130 * 60
    return round(seconds), "estimated"


def audit(path: Path) -> dict[str, object]:
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        slides = sorted(
            (name for name in names if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)),
            key=natural_key,
        )
        notes = sorted(
            (name for name in names if re.fullmatch(r"ppt/notesSlides/notesSlide\d+\.xml", name)),
            key=natural_key,
        )
        media = [name for name in names if name.startswith("ppt/media/") and not name.endswith("/")]

        slide_texts = [xml_text(archive.read(name)) for name in slides]
        note_texts = [xml_text(archive.read(name)) for name in notes]
        padded_notes = note_texts + [""] * max(0, len(slides) - len(note_texts))

        fonts: Counter[str] = Counter()
        for name in names:
            if not name.endswith(".xml") or not name.startswith("ppt/"):
                continue
            try:
                root = ET.fromstring(archive.read(name))
            except ET.ParseError:
                continue
            for node in root.iter():
                typeface = node.attrib.get("typeface")
                if typeface:
                    fonts[typeface] += 1

        width_in = height_in = None
        if "ppt/presentation.xml" in names:
            root = ET.fromstring(archive.read("ppt/presentation.xml"))
            size = root.find("p:sldSz", NS)
            if size is not None:
                width_in = round(int(size.attrib["cx"]) / 914400, 3)
                height_in = round(int(size.attrib["cy"]) / 914400, 3)

        placeholders = []
        for index, text in enumerate(slide_texts, start=1):
            lowered = text.lower()
            hits = [pattern for pattern in PLACEHOLDER_PATTERNS if pattern in lowered]
            if hits:
                placeholders.append({"slide": index, "patterns": hits})

        media_types = Counter(Path(name).suffix.lower() or "no-extension" for name in media)
        timing = []
        backup_slides = []
        for index, (slide_text, note_text) in enumerate(
            zip(slide_texts, padded_notes, strict=False), start=1
        ):
            is_backup = any(marker in note_text for marker in BACKUP_MARKERS)
            if not is_backup and ("备用页" in slide_text or re.search(r"\bbackup\b", slide_text, re.I)):
                is_backup = True
            seconds, source = estimate_seconds(note_text)
            timing.append(
                {
                    "slide": index,
                    "backup": is_backup,
                    "seconds": seconds,
                    "timing_source": source,
                }
            )
            if is_backup:
                backup_slides.append(index)
        main_seconds = sum(item["seconds"] for item in timing if not item["backup"])
        return {
            "file": str(path.resolve()),
            "bytes": path.stat().st_size,
            "slide_count": len(slides),
            "slide_size_inches": [width_in, height_in],
            "notes_count": len(notes),
            "notes_with_script": sum("【讲稿】" in text for text in note_texts),
            "notes_with_sources": sum("[Sources]" in text for text in note_texts),
            "empty_or_short_notes": [
                index for index, text in enumerate(note_texts, start=1) if len(text.strip()) < 40
            ],
            "media_count": len(media),
            "media_types": dict(sorted(media_types.items())),
            "fonts": dict(fonts.most_common()),
            "placeholder_hits": placeholders,
            "main_slide_count": len(slides) - len(backup_slides),
            "backup_slide_count": len(backup_slides),
            "backup_slides": backup_slides,
            "estimated_main_minutes": round(main_seconds / 60, 2),
            "timing_by_slide": timing,
        }


def strict_failures(
    report: dict[str, object],
    target_minutes: float | None = None,
    time_tolerance: float = 0.2,
    target_main_slides: int | None = None,
    slide_tolerance: int = 1,
    require_backup: bool = False,
) -> list[str]:
    failures = []
    slides = int(report["slide_count"])
    if slides == 0:
        failures.append("No slides found")
    if int(report["notes_count"]) != slides:
        failures.append("Not every slide has a notes part")
    if int(report["notes_with_script"]) != slides:
        failures.append("Not every slide contains 【讲稿】")
    if int(report["notes_with_sources"]) != slides:
        failures.append("Not every slide contains [Sources]")
    if report["placeholder_hits"]:
        failures.append("Placeholder text remains")
    if require_backup and int(report["backup_slide_count"]) == 0:
        failures.append("Backup slides were required but none were marked")
    if target_minutes is not None:
        estimated = float(report["estimated_main_minutes"])
        low = target_minutes * (1 - time_tolerance)
        high = target_minutes * (1 + time_tolerance)
        if not low <= estimated <= high:
            failures.append(
                f"Estimated main talk is {estimated:.2f} min; target range is {low:.2f}–{high:.2f} min"
            )
    if target_main_slides is not None:
        actual = int(report["main_slide_count"])
        low = max(1, target_main_slides - slide_tolerance)
        high = target_main_slides + slide_tolerance
        if not low <= actual <= high:
            failures.append(
                f"Main deck has {actual} slides; target range is {low}–{high} slides"
            )
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--json", action="store_true", help="Print JSON only")
    parser.add_argument("--strict", action="store_true", help="Fail final-deck requirements")
    parser.add_argument("--target-minutes", type=float, help="Target duration for main slides")
    parser.add_argument("--target-main-slides", type=int, help="Target number of non-backup slides")
    parser.add_argument(
        "--time-tolerance",
        type=float,
        default=0.2,
        help="Allowed fractional deviation from target duration (default: 0.2)",
    )
    parser.add_argument(
        "--require-backup",
        action="store_true",
        help="Require at least one slide marked 【备用页】 or [Backup]",
    )
    parser.add_argument(
        "--slide-tolerance",
        type=int,
        default=1,
        help="Allowed absolute deviation from target main-slide count (default: 1)",
    )
    args = parser.parse_args()

    if not args.pptx.is_file():
        parser.error(f"File not found: {args.pptx}")
    if args.pptx.suffix.lower() != ".pptx":
        parser.error("Input must be a .pptx file")
    if args.target_minutes is not None and args.target_minutes <= 0:
        parser.error("--target-minutes must be positive")
    if args.target_main_slides is not None and args.target_main_slides <= 0:
        parser.error("--target-main-slides must be positive")
    if not 0 <= args.time_tolerance <= 1:
        parser.error("--time-tolerance must be between 0 and 1")
    if args.slide_tolerance < 0:
        parser.error("--slide-tolerance must be zero or positive")

    try:
        report = audit(args.pptx)
    except zipfile.BadZipFile:
        parser.error("Input is not a valid PPTX/ZIP package")

    failures = (
        strict_failures(
            report,
            target_minutes=args.target_minutes,
            time_tolerance=args.time_tolerance,
            target_main_slides=args.target_main_slides,
            slide_tolerance=args.slide_tolerance,
            require_backup=args.require_backup,
        )
        if args.strict
        else []
    )
    report["strict_failures"] = failures

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"File: {report['file']}")
        print(f"Slides: {report['slide_count']} | Notes: {report['notes_count']}")
        print(
            "Notes markers: "
            f"script {report['notes_with_script']}/{report['slide_count']}, "
            f"sources {report['notes_with_sources']}/{report['slide_count']}"
        )
        print(f"Media: {report['media_count']} {report['media_types']}")
        print(
            f"Main slides: {report['main_slide_count']} | "
            f"Backup slides: {report['backup_slide_count']} {report['backup_slides']}"
        )
        print(f"Estimated main talk: {report['estimated_main_minutes']} minutes")
        print(f"Fonts: {report['fonts']}")
        print(f"Placeholder hits: {report['placeholder_hits'] or 'none'}")
        print(f"Strict failures: {failures or 'none'}")

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
