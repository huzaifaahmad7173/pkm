#!/usr/bin/env python3
"""Validate YAML frontmatter of Knowledge/*.md files against schema.yaml."""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent.parent
SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schema.yaml"
KNOWLEDGE_DIR = REPO_ROOT / "Knowledge"

TAG_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

SMALL_WORDS = {"a", "an", "and", "as", "at", "but", "by", "for", "in", "nor",
               "of", "on", "or", "so", "the", "to", "up", "yet"}


def is_title_case(s: str) -> bool:
    """Check if string is in Title Case. Allows acronyms and lowercase conjunctions/prepositions."""
    for word in s.split():
        if not word:
            continue
        if word.isupper():
            continue
        if word.lower() in SMALL_WORDS:
            continue
        if not word[0].isupper():
            return False
    return True


def parse_yaml_simple(text: str) -> dict:
    """Parse a minimal YAML subset: scalars, inline lists, and block lists."""
    result = {}
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line or line.startswith("#"):
            i += 1
            continue
        match = re.match(r"^(\w[\w\s]*):\s*(.*)", line)
        if not match:
            i += 1
            continue
        key = match.group(1).strip()
        value = match.group(2).strip()

        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            result[key] = [item.strip().strip('"').strip("'") for item in inner.split(",") if item.strip()]
        elif value == "":
            items = []
            i += 1
            while i < len(lines):
                stripped = lines[i].strip()
                if stripped.startswith("- "):
                    items.append(stripped[2:].strip().strip('"').strip("'"))
                    i += 1
                else:
                    break
            result[key] = items
        else:
            result[key] = value.strip('"').strip("'")
        i += 1
    return result


def load_schema() -> dict:
    """Load schema.yaml using the minimal parser."""
    text = SCHEMA_PATH.read_text(encoding="utf-8")
    raw = parse_yaml_simple(text)
    return {
        "required_fields": raw.get("required_fields", []),
        "optional_fields": raw.get("optional_fields", []),
        "allowed_status": raw.get("allowed_status", []),
    }


def extract_frontmatter(filepath: Path) -> str | None:
    """Extract YAML frontmatter block from a Markdown file. Returns None if absent."""
    text = filepath.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    end = -1
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end == -1:
        return None
    return "\n".join(lines[1:end])


def validate_file(filepath: Path, schema: dict) -> tuple[bool, list[str]]:
    """Validate a single file. Returns (is_valid, list_of_findings)."""
    rel = str(filepath.relative_to(REPO_ROOT))
    raw_fm = extract_frontmatter(filepath)
    if raw_fm is None:
        return False, [f"INVALID — {rel}\n  1. [MISSING] No frontmatter block found"]

    frontmatter = parse_yaml_simple(raw_fm)
    required = schema["required_fields"]
    optional = schema["optional_fields"]
    allowed = set(required + optional)
    allowed_status = schema["allowed_status"]

    findings = []
    num = 1

    for field in required:
        if field not in frontmatter:
            findings.append(f"{num}. [MISSING] Required field `{field}` not found")
            num += 1

    for key in frontmatter:
        if key not in allowed:
            findings.append(f"{num}. [UNEXPECTED] Field `{key}` is not in the allowed schema")
            num += 1

    title = frontmatter.get("title")
    if title is not None:
        if not isinstance(title, str) or not title:
            findings.append(f"{num}. [INVALID VALUE] `title` — must be a non-empty string")
            num += 1
        elif not is_title_case(title):
            findings.append(f"{num}. [INVALID VALUE] `title` = `{title}` — not in Title Case")
            num += 1

    desc = frontmatter.get("description")
    if desc is not None:
        if not isinstance(desc, str) or not desc:
            findings.append(f"{num}. [INVALID VALUE] `description` — must be a non-empty string")
            num += 1
        elif not desc.endswith("."):
            findings.append(f"{num}. [INVALID VALUE] `description` — must end with `.`")
            num += 1

    tags = frontmatter.get("tags")
    if tags is not None:
        if not isinstance(tags, list) or len(tags) == 0:
            findings.append(f"{num}. [INVALID VALUE] `tags` — must be a non-empty list")
            num += 1
        else:
            for tag in tags:
                if not TAG_PATTERN.match(tag):
                    findings.append(f"{num}. [INVALID VALUE] `tags` item `{tag}` — must be kebab-case (lowercase alphanumeric with hyphens)")
                    num += 1

    status = frontmatter.get("status")
    if status is not None:
        if status not in allowed_status:
            findings.append(f"{num}. [INVALID VALUE] `status` = `{status}` — must be one of: {', '.join(allowed_status)}")
            num += 1

    related = frontmatter.get("related")
    if related is not None:
        if not isinstance(related, list):
            findings.append(f"{num}. [INVALID VALUE] `related` — must be a list")
            num += 1
        else:
            for item in related:
                if "/" in item or ".." in item or item.startswith("."):
                    findings.append(f"{num}. [INVALID VALUE] `related` item `{item}` — must be a bare .md filename")
                    num += 1

    is_valid = len(findings) == 0
    header = f"{'VALID' if is_valid else 'INVALID'} — {rel}"
    if is_valid:
        body = "  All required fields present. No unexpected fields. Values conform to schema."
        return True, [f"{header}\n{body}"]
    else:
        return False, [f"{header}"] + [f"  {f}" for f in findings]


def main():
    schema = load_schema()

    targets = sorted(REPO_ROOT.rglob("*.md"))
    targets = [f for f in targets if f.name != "AGENTS.md" and ".opencode" not in f.parts and "Templates" not in f.parts]

    all_valid = True
    for fp in targets:
        valid, lines = validate_file(fp, schema)
        print("\n".join(lines))
        if not valid:
            all_valid = False

    print(f"\n--- {len(targets)} files checked ---")
    sys.exit(0 if all_valid else 1)


if __name__ == "__main__":
    main()