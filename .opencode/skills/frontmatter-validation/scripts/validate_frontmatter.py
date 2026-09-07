

import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[4]
SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schema.yaml"

TAG_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

SMALL_WORDS = {
    "a", "an", "and", "as", "at", "but", "by",
    "for", "in", "nor", "of", "on", "or", "so",
    "the", "to", "up", "yet"
}


def is_title_case(text: str) -> bool:
    for word in text.split():
        if word.isupper() or word.lower() in SMALL_WORDS:
            continue
        if not word[0].isupper():
            return False
    return True


def load_schema() -> dict:
    with open(SCHEMA_PATH, encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    return {
        "required_fields": raw.get("required_fields", []),
        "optional_fields": raw.get("optional_fields", []),
        "allowed_status": raw["fields"]["status"]["allowed_values"],
    }


def extract_frontmatter(filepath: Path) -> str | None:
    lines = filepath.read_text(encoding="utf-8").splitlines()

    if not lines or lines[0].strip() != "---":
        return None

    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i])

    return None


def _quote_colons(text: str) -> str:
    result = []
    for line in text.splitlines():
        match = re.match(r"^(\w[\w\s]*):\s+(.*)", line)
        if match and ":" in match.group(2):
            key, value = match.group(1), match.group(2)
            result.append(f'{key}: "{value}"')
        else:
            result.append(line)
    return "\n".join(result)


def validate_file(filepath: Path, schema: dict) -> tuple[bool, list[str]]:
    relative = filepath.relative_to(REPO_ROOT)
    raw_frontmatter = extract_frontmatter(filepath)

    if raw_frontmatter is None:
        return False, [
            f"INVALID — {relative}",
            "  1. [MISSING] No frontmatter block found",
        ]

    docs = list(yaml.safe_load_all(_quote_colons(raw_frontmatter)))
    frontmatter = docs[0] if docs else {}

    required = schema["required_fields"]
    optional = schema["optional_fields"]
    allowed_fields = set(required + optional)
    allowed_status = schema["allowed_status"]

    errors = []

    for field in required:
        if field not in frontmatter:
            errors.append(f"[MISSING] Required field `{field}` not found")

    for field in frontmatter:
        if field not in allowed_fields:
            errors.append(f"[UNEXPECTED] Field `{field}` is not allowed")

    title = frontmatter.get("title")
    if title is not None:
        if not isinstance(title, str) or not title:
            errors.append("[INVALID VALUE] `title` must be a non-empty string")
        elif not is_title_case(title):
            errors.append(f"[INVALID VALUE] `title` = `{title}` is not Title Case")

    description = frontmatter.get("description")
    if description is not None:
        if not isinstance(description, str) or not description:
            errors.append("[INVALID VALUE] `description` must be a non-empty string")
        elif not description.endswith("."):
            errors.append("[INVALID VALUE] `description` must end with `.`")

    tags = frontmatter.get("tags")
    if tags is not None:
        if not isinstance(tags, list) or not tags:
            errors.append("[INVALID VALUE] `tags` must be a non-empty list")
        else:
            for tag in tags:
                if not TAG_PATTERN.fullmatch(tag):
                    errors.append(f"[INVALID VALUE] tag `{tag}` must be kebab-case")

    status = frontmatter.get("status")
    if status is not None and status not in allowed_status:
        errors.append(
            f"[INVALID VALUE] `status` must be one of: "
            f"{', '.join(allowed_status)}"
        )

    related = frontmatter.get("related")
    if related is not None:
        if not isinstance(related, list):
            errors.append("[INVALID VALUE] `related` must be a list")
        else:
            for item in related:
                if "/" in item or ".." in item or item.startswith("."):
                    errors.append(
                        f"[INVALID VALUE] related item `{item}` "
                        "must be a bare filename"
                    )

    if errors:
        return False, [
            f"INVALID — {relative}",
            *[f"  {i}. {error}" for i, error in enumerate(errors, 1)]
        ]

    return True, [
        f"VALID — {relative}",
        "  All fields conform to schema."
    ]


def main() -> None:
    schema = load_schema()

    files = [
        f for f in REPO_ROOT.rglob("*.md")
        if f.name != "AGENTS.md"
        and ".opencode" not in f.parts
        and "Templates" not in f.parts
    ]

    all_valid = True

    for filepath in sorted(files):
        valid, messages = validate_file(filepath, schema)
        print("\n".join(messages))
        if not valid:
            all_valid = False

    print(f"\n--- {len(files)} files checked ---")
    sys.exit(0 if all_valid else 1)


if __name__ == "__main__":
    main()
