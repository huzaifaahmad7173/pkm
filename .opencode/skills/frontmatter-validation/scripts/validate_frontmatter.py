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


def extract_frontmatter_from_codeblock(filepath: Path) -> str | None:
    """Extract frontmatter that is wrapped in markdown code block markers."""
    text = filepath.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines:
        return None
    first = lines[0].strip()
    if not first.startswith("```"):
        return None
    fm_start = 1
    fm_end = -1
    for i in range(1, len(lines)):
        if lines[i].strip() == "```":
            fm_end = i
            break
    if fm_end != -1:
        inner = "\n".join(lines[fm_start:fm_end])
        if extract_frontmatter_from_string(inner) is not None:
            return inner
    else:
        rest = "\n".join(lines[fm_start:])
        if extract_frontmatter_from_string(rest) is not None:
            return rest
    return None


def extract_frontmatter_from_string(text: str) -> str | None:
    """Extract YAML frontmatter from a string that starts with ---."""
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


def extract_title_from_content(filepath: Path) -> str | None:
    """Extract title from first H1 heading in file content."""
    text = filepath.read_text(encoding="utf-8")
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# ") and not stripped.startswith("## "):
            return stripped[2:].strip()
    return None


def extract_description_from_content(filepath: Path) -> str | None:
    """Extract description from first non-empty, non-heading line after H1."""
    text = filepath.read_text(encoding="utf-8")
    lines = text.splitlines()
    found_h1 = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# ") and not stripped.startswith("## "):
            found_h1 = True
            continue
        if found_h1:
            if not stripped:
                continue
            if stripped.startswith("#"):
                break
            if stripped.startswith("```"):
                break
            return stripped
    return None


def build_frontmatter_from_content(filepath: Path) -> dict:
    """Build frontmatter dict by extracting info from file content."""
    title = extract_title_from_content(filepath)
    description = extract_description_from_content(filepath)

    parts = filepath.relative_to(REPO_ROOT).parts
    domain = parts[1] if len(parts) > 1 else "unknown"
    stem = filepath.stem

    tags = [domain, stem]
    description_text = description if description else "TODO: Add description."
    if not description_text.endswith("."):
        description_text += "."

    return {
        "title": title if title else "TODO: Add Title",
        "description": description_text,
        "tags": tags,
        "status": "Draft",
    }


def format_frontmatter(fm: dict) -> str:
    """Format a frontmatter dict as a YAML block string."""
    lines = ["---"]
    lines.append(f"title: {fm['title']}")
    lines.append(f"description: {fm['description']}")
    lines.append("tags:")
    for tag in fm.get("tags", []):
        lines.append(f"  - {tag}")
    lines.append(f"status: {fm.get('status', 'Draft')}")
    related = fm.get("related")
    if related:
        lines.append("related:")
        for item in related:
            lines.append(f"  - {item}")
    lines.append("---")
    return "\n".join(lines)


def fix_file_no_frontmatter(filepath: Path) -> str:
    """Fix a file that has no frontmatter by inserting one derived from content."""
    fm = build_frontmatter_from_content(filepath)
    fm_block = format_frontmatter(fm)
    text = filepath.read_text(encoding="utf-8")

    lines = text.splitlines(keepends=True)
    insert_at = 0
    for i, line in enumerate(lines):
        if line.strip().startswith("# ") and not line.strip().startswith("## "):
            insert_at = i
            break

    new_text = fm_block + "\n\n" + "".join(lines[insert_at:])
    filepath.write_text(new_text, encoding="utf-8")
    return "inserted frontmatter from content"


def fix_file_codeblock_frontmatter(filepath: Path) -> str:
    """Fix a file that has frontmatter wrapped in code block markers."""
    text = filepath.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    fm_start = 0
    fm_end = -1
    for i, line in enumerate(lines):
        if line.strip().startswith("```") and i == 0:
            fm_start = 1
        if line.strip() == "```" and i > 0:
            fm_end = i
            break

    if fm_end != -1:
        inner_lines = lines[fm_start:fm_end]
        rest_lines = lines[fm_end + 1:]
        new_lines = inner_lines + rest_lines
    else:
        rest_lines = lines[fm_start:]
        new_lines = rest_lines

    filepath.write_text("".join(new_lines), encoding="utf-8")
    return "stripped code block markers from frontmatter"


def fix_file(filepath: Path) -> str:
    """Fix a single invalid file. Returns description of what was done."""
    raw_fm = extract_frontmatter(filepath)
    if raw_fm is not None:
        return "already has valid frontmatter (skipped)"

    codeblock_fm = extract_frontmatter_from_codeblock(filepath)
    if codeblock_fm is not None:
        return fix_file_codeblock_frontmatter(filepath)

    return fix_file_no_frontmatter(filepath)


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


def prompt_fix(invalid_files: list[Path]) -> None:
    """Ask user if they want to fix invalid files, then fix selected ones."""
    count = len(invalid_files)
    print(f"\nFound {count} invalid file(s). Would you like to fix them? [y/N]")
    answer = input("> ").strip().lower()

    if answer != "y":
        print("Skipping fixes.")
        return

    print()
    for i, fp in enumerate(invalid_files, 1):
        rel = str(fp.relative_to(REPO_ROOT))
        print(f"  {i}. {rel}")

    print("\nEnter file numbers to fix (comma-separated) or 'all':")
    selection = input("> ").strip().lower()

    if selection == "all":
        selected = list(range(count))
    else:
        selected = []
        for part in selection.split(","):
            part = part.strip()
            if part.isdigit():
                idx = int(part) - 1
                if 0 <= idx < count:
                    selected.append(idx)

    if not selected:
        print("No valid files selected. Skipping fixes.")
        return

    print()
    fixed = 0
    for idx in selected:
        fp = invalid_files[idx]
        rel = str(fp.relative_to(REPO_ROOT))
        result = fix_file(fp)
        print(f"Fixed: {rel} ({result})")
        fixed += 1

    print(f"\n--- {fixed} file(s) fixed ---")


def main():
    schema = load_schema()

    targets = sorted(REPO_ROOT.rglob("*.md"))
    targets = [f for f in targets if f.name != "AGENTS.md" and ".opencode" not in f.parts and "Templates" not in f.parts]

    all_valid = True
    invalid_files = []
    for fp in targets:
        valid, lines = validate_file(fp, schema)
        print("\n".join(lines))
        if not valid:
            all_valid = False
            invalid_files.append(fp)

    print(f"\n--- {len(targets)} files checked ---")

    if invalid_files:
        prompt_fix(invalid_files)

    sys.exit(0 if all_valid else 1)


if __name__ == "__main__":
    main()
