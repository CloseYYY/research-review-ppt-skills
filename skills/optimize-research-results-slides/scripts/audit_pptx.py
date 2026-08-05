#!/usr/bin/env python3
"""Audit a result-driven lab-meeting PPTX using only the Python standard library."""

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
RESULT_FIELDS = ("实验目的", "实验方法", "实验结果", "一句话结论")
EXPECTED_PLACEHOLDERS = (
    "待确认",
    "待补：图片",
    "待补：名称",
    "待补：数值",
    "待补：结论",
    "待补：一句话结论",
)
UNINTENDED_PLACEHOLDERS = (
    "todo",
    "tbd",
    "lorem ipsum",
    "click to add",
    "单击此处添加",
    "双击此处添加",
)
COMMON_TERMS = {"DNA", "RNA", "PCR", "FACS", "WB"}
TIME_PATTERN = re.compile(r"【建议时长】\s*(\d+(?:\.\d+)?)\s*(?:秒|s|sec)", re.I)
TYPE_PATTERN = re.compile(r"【页面类型】\s*(封面|背景页|研究问题|结果页|阶段总结|未来计划|备用页|其他)")
TERM_PATTERN = re.compile(r"\b[A-Z][A-Z0-9-]{1,9}\b")


def natural_key(value: str) -> list[object]:
    return [int(part) if part.isdigit() else part for part in re.split(r"(\d+)", value)]


def parse_xml(data: bytes) -> ET.Element | None:
    try:
        return ET.fromstring(data)
    except ET.ParseError:
        return None


def xml_text(data: bytes) -> str:
    root = parse_xml(data)
    if root is None:
        return ""
    return "\n".join(node.text or "" for node in root.findall(".//a:t", NS))


def estimate_seconds(note_text: str) -> tuple[int, str]:
    explicit = TIME_PATTERN.search(note_text)
    if explicit:
        return round(float(explicit.group(1))), "explicit"
    talk = note_text.split("[Sources]", 1)[0]
    talk = re.sub(r"【(?:页面类型|讲稿|建议时长|首次术语)】[^\n]*", "", talk)
    chinese = len(re.findall(r"[\u3400-\u9fff]", talk))
    english = len(
        re.findall(
            r"[A-Za-z0-9]+(?:[-–/][A-Za-z0-9]+)*",
            re.sub(r"[\u3400-\u9fff]", " ", talk),
        )
    )
    return round(chinese / 240 * 60 + english / 130 * 60), "estimated"


def page_type(note_text: str) -> str | None:
    match = TYPE_PATTERN.search(note_text)
    return match.group(1) if match else None


def background_colors(root: ET.Element | None) -> list[str]:
    if root is None:
        return []
    colors = []
    for bg in root.findall(".//p:bg", NS):
        for node in bg.findall(".//a:srgbClr", NS):
            value = node.attrib.get("val", "").upper()
            if value:
                colors.append(value)
        for node in bg.findall(".//a:schemeClr", NS):
            value = node.attrib.get("val", "")
            if value:
                colors.append(f"scheme:{value}")
    return colors


def collect_line_spacing(root: ET.Element | None) -> list[int]:
    if root is None:
        return []
    values = []
    for node in root.findall(".//a:lnSpc/a:spcPct", NS):
        try:
            values.append(int(node.attrib["val"]))
        except (KeyError, ValueError):
            continue
    return values


def relationship_risks(archive: zipfile.ZipFile) -> tuple[list[dict[str, str]], list[str]]:
    external = []
    for name in archive.namelist():
        if not name.endswith(".rels"):
            continue
        root = parse_xml(archive.read(name))
        if root is None:
            continue
        for rel in root:
            if rel.attrib.get("TargetMode") == "External":
                external.append({"part": name, "target": rel.attrib.get("Target", "")})
    embedded = [
        name
        for name in archive.namelist()
        if name.startswith("ppt/embeddings/") and not name.endswith("/")
    ]
    return external, embedded


def audit(path: Path) -> dict[str, object]:
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        slides = sorted(
            (name for name in names if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)),
            key=natural_key,
        )
        notes = sorted(
            (
                name
                for name in names
                if re.fullmatch(r"ppt/notesSlides/notesSlide\d+\.xml", name)
            ),
            key=natural_key,
        )
        slide_texts = [xml_text(archive.read(name)) for name in slides]
        note_texts = [xml_text(archive.read(name)) for name in notes]
        padded_notes = note_texts + [""] * max(0, len(slides) - len(note_texts))

        fonts: Counter[str] = Counter()
        line_spacing = []
        slide_backgrounds = []
        for index, name in enumerate(slides, start=1):
            root = parse_xml(archive.read(name))
            line_spacing.extend(
                {"slide": index, "value": value}
                for value in collect_line_spacing(root)
            )
            colors = background_colors(root)
            if colors:
                slide_backgrounds.append({"slide": index, "colors": colors})
        # Count only explicit typefaces used by visible slide text. Theme, master,
        # and notes defaults may legitimately retain Office fallback fonts.
        for name in slides:
            root = parse_xml(archive.read(name))
            if root is None:
                continue
            for node in root.iter():
                font = node.attrib.get("typeface")
                if font and not font.startswith("+"):
                    fonts[font] += 1

        result_issues = []
        note_issues = []
        placeholder_hits = []
        timing = []
        page_type_counts: Counter[str] = Counter()
        term_candidates = []
        seen_terms: set[str] = set()
        for index, (slide_text, note_text) in enumerate(
            zip(slide_texts, padded_notes, strict=False), start=1
        ):
            current_type = page_type(note_text)
            if current_type:
                page_type_counts[current_type] += 1
            missing_markers = [
                marker
                for marker in ("【页面类型】", "【讲稿】", "【建议时长】", "[Sources]")
                if marker not in note_text
            ]
            if missing_markers:
                note_issues.append({"slide": index, "missing": missing_markers})
            if current_type == "结果页":
                missing = [field for field in RESULT_FIELDS if field not in slide_text]
                if missing:
                    result_issues.append({"slide": index, "missing": missing})
            lowered = slide_text.lower()
            unintended = [value for value in UNINTENDED_PLACEHOLDERS if value in lowered]
            expected = [value for value in EXPECTED_PLACEHOLDERS if value in slide_text]
            if unintended or expected:
                placeholder_hits.append(
                    {"slide": index, "unintended": unintended, "expected": expected}
                )
            seconds, source = estimate_seconds(note_text)
            timing.append(
                {
                    "slide": index,
                    "page_type": current_type,
                    "seconds": seconds,
                    "source": source,
                }
            )
            for term in TERM_PATTERN.findall(slide_text):
                if term in COMMON_TERMS or re.fullmatch(r"P\d+", term) or term in seen_terms:
                    continue
                seen_terms.add(term)
                expanded = term in note_text and (
                    "【首次术语】" in note_text
                    or re.search(
                        rf"[（(][^）)]*\b{re.escape(term)}\b[^）)]*[）)]",
                        note_text,
                    )
                )
                term_candidates.append(
                    {
                        "slide": index,
                        "term": term,
                        "expanded_in_notes": bool(expanded),
                    }
                )

        external, embedded = relationship_risks(archive)
        comments = [
            name
            for name in names
            if name.startswith("ppt/comments/")
            or name.startswith("ppt/commentAuthors")
        ]
        main_timing = [item for item in timing if item["page_type"] != "备用页"]
        main_seconds = sum(int(item["seconds"]) for item in main_timing)
        nonwhite = [
            item
            for item in slide_backgrounds
            if any(
                color not in {"FFFFFF", "scheme:bg1", "scheme:lt1"}
                for color in item["colors"]
            )
        ]
        spacing_outliers = [
            item
            for item in line_spacing
            if not 120000 <= int(item["value"]) <= 150000
        ]
        return {
            "file": str(path.resolve()),
            "slide_count": len(slides),
            "notes_count": len(notes),
            "page_type_counts": dict(page_type_counts),
            "result_field_issues": result_issues,
            "note_issues": note_issues,
            "placeholder_hits": placeholder_hits,
            "fonts": dict(fonts.most_common()),
            "slide_backgrounds": slide_backgrounds,
            "nonwhite_explicit_backgrounds": nonwhite,
            "line_spacing_values": line_spacing,
            "line_spacing_outliers": spacing_outliers,
            "term_expansion_candidates": term_candidates,
            "external_relationships": external,
            "embedded_files": embedded,
            "comment_parts": comments,
            "main_slide_count": len(main_timing),
            "estimated_main_minutes": round(main_seconds / 60, 2),
            "timing_by_slide": timing,
        }


def strict_failures(report: dict[str, object], args: argparse.Namespace) -> list[str]:
    failures = []
    slides = int(report["slide_count"])
    if slides == 0:
        failures.append("No slides found")
    if int(report["notes_count"]) != slides:
        failures.append("Not every slide has a notes part")
    if report["note_issues"]:
        failures.append("Required note markers are missing")
    if report["result_field_issues"]:
        failures.append("A result slide is missing one or more required visible fields")
    if any(item["unintended"] for item in report["placeholder_hits"]):
        failures.append("Unintended template placeholder text remains")
    if report["external_relationships"]:
        failures.append("External relationships remain in the PPTX")
    if report["embedded_files"]:
        failures.append("Embedded files remain in the PPTX")
    if report["comment_parts"]:
        failures.append("Comments remain in the PPTX")
    if args.require_white_background and report["nonwhite_explicit_backgrounds"]:
        failures.append("A slide has an explicit non-white background")
    if args.required_font:
        used = set(report["fonts"])
        disallowed = sorted(
            font
            for font in used
            if font.casefold() != args.required_font.casefold()
        )
        if disallowed:
            failures.append(
                f"Fonts other than {args.required_font!r} remain: {', '.join(disallowed)}"
            )
    if args.require_line_spacing and report["line_spacing_outliers"]:
        failures.append("Explicit line spacing falls outside 1.2–1.5")
    if args.strict_terms and any(
        not item["expanded_in_notes"]
        for item in report["term_expansion_candidates"]
    ):
        failures.append("An uncommon abbreviation may lack first-use expansion in notes")
    if args.target_minutes is not None:
        actual = float(report["estimated_main_minutes"])
        low, high = args.target_minutes * 0.8, args.target_minutes * 1.2
        if not low <= actual <= high:
            failures.append(
                f"Estimated main talk is {actual:.2f} min; target range is {low:.2f}–{high:.2f} min"
            )
    if args.target_main_slides is not None:
        actual = int(report["main_slide_count"])
        if not max(1, args.target_main_slides - 1) <= actual <= args.target_main_slides + 1:
            failures.append(
                f"Main deck has {actual} slides; expected {args.target_main_slides} ± 1"
            )
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--require-white-background", action="store_true")
    parser.add_argument("--required-font")
    parser.add_argument("--require-line-spacing", action="store_true")
    parser.add_argument("--strict-terms", action="store_true")
    parser.add_argument("--target-minutes", type=float)
    parser.add_argument("--target-main-slides", type=int)
    args = parser.parse_args()
    if not args.pptx.is_file() or args.pptx.suffix.lower() != ".pptx":
        parser.error("Input must be an existing .pptx file")
    try:
        report = audit(args.pptx)
    except zipfile.BadZipFile:
        parser.error("Input is not a valid PPTX/ZIP package")
    failures = strict_failures(report, args) if args.strict else []
    report["strict_failures"] = failures
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"File: {report['file']}")
        print(f"Slides: {report['slide_count']} | Notes: {report['notes_count']}")
        print(f"Types: {report['page_type_counts']}")
        print(f"Result issues: {report['result_field_issues'] or 'none'}")
        print(f"Note issues: {report['note_issues'] or 'none'}")
        print(f"Expected/unintended placeholders: {report['placeholder_hits'] or 'none'}")
        print(f"Fonts: {report['fonts']}")
        print(f"Non-white explicit backgrounds: {report['nonwhite_explicit_backgrounds'] or 'none'}")
        print(f"Line-spacing outliers: {report['line_spacing_outliers'] or 'none'}")
        print(f"External relationships: {report['external_relationships'] or 'none'}")
        print(
            f"Embedded files: {report['embedded_files'] or 'none'} | "
            f"Comments: {report['comment_parts'] or 'none'}"
        )
        print(f"Estimated main talk: {report['estimated_main_minutes']} minutes")
        print(f"Strict failures: {failures or 'none'}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
