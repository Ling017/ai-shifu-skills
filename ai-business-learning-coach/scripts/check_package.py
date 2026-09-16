#!/usr/bin/env python3
"""Offline integrity checks for this Skill; not a learning-effect test."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
def check(condition, message):
    if not condition:
        errors.append(message)
def read_json(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))

def main():
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    check(text.startswith("---\n"), "Missing frontmatter")
    match = re.search(r"^name: ([a-z0-9-]+)$", text, re.M)
    check(match is not None and match.group(1) == ROOT.name, "Skill name/directory mismatch")
    index = read_json("course-index.json")
    check(index["name"] == ROOT.name, "Index name mismatch")
    sources = read_json("source-map.json")
    for entry in sources["files"]:
        path = ROOT / entry["output"]
        check(path.is_file(), "Missing source: " + entry["output"])
        if path.is_file():
            check(hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"], "Source hash mismatch: " + entry["output"])
    section_ids = set()
    interaction_ids = set()
    for section in index["sections"]:
        check(section["id"] not in section_ids, "Duplicate section id")
        section_ids.add(section["id"])
        body = (ROOT / section["file"]).read_text(encoding="utf-8")
        for interaction in section["interactions"]:
            check(interaction["id"] not in interaction_ids, "Duplicate interaction id")
            interaction_ids.add(interaction["id"])
            check(body[interaction["offset"]:interaction["end_offset"]] == interaction["raw"], "Interaction/source mismatch: " + interaction["id"])
    for filename in ["navigation.json", "supplementary-navigation.json"]:
        for entry in read_json(filename)["lessons"]:
            course = entry.get("course_id") or entry.get("course_bid") or sources["source_url"].rsplit("/", 1)[-1]
            lesson = entry.get("lesson_id") or entry.get("outline_bid")
            link = entry.get("deep_link")
            if link:
                check(link == "https://app.ai-shifu.cn/c/" + course + "?lessonid=" + lesson, "Navigation mapping mismatch")
    for path in ROOT.rglob("*.md"):
        body = path.read_text(encoding="utf-8")
        check(not re.search(r"/(Users|private/var|tmp)/", body), "Local absolute path: " + path.name)
        for target in re.findall(r"\]\(([^)]+)\)", body):
            if target.startswith(("https:", "http:", "#")):
                continue
            check((path.parent / target.split("#")[0]).is_file(), "Broken local reference: " + path.name + " -> " + target)
    example = read_json("state-example.json")
    check(example["progress"]["answers"] == {} and example["progress"]["variables"] == {} and example["progress"]["completed_sections"] == [], "Populated progress example")
    check(example["profile"]["facts"] == [] and example["practice"]["sessions"] == [], "Populated learner example")
    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        check(path.name not in {".env", "credentials.json", "progress.json", "profile.json", "practice.json", ".course-learning"}, "Private state/config present: " + path.name)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"PASS: {len(section_ids)} source lessons, {len(interaction_ids)} interactions, hashes, references and empty state example")
    print("This is an offline structural check, not a security audit or learning-effect evaluation.")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, KeyError, ValueError) as exc:
        print(f"Check failed: {exc}", file=sys.stderr)
        sys.exit(1)
