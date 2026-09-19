#!/usr/bin/env python3
import os
import subprocess
import sys
from pathlib import Path
from importlib.metadata import version, PackageNotFoundError

import yaml

SKILL_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = Path(__file__).resolve().parents[4]


def load_checks():
    return yaml.safe_load((SKILL_DIR / "checks.yaml").read_text())


def run(cmd):
    try:
        return subprocess.check_output(cmd.split(), stderr=subprocess.STDOUT, text=True).strip()
    except Exception:
        return None


def parse_version(v):
    return [int(x) for x in v.split(".")]


def version_ok(installed, constraint):
    installed_v = parse_version(installed)
    if constraint.startswith(">="):
        return installed_v >= parse_version(constraint[2:])
    if constraint.startswith("<="):
        return installed_v <= parse_version(constraint[2:])
    if constraint.startswith("=="):
        return installed_v == parse_version(constraint[2:])
    return True


def main():
    checks = load_checks()
    passed = failed = 0

    print("=== Environment Dependency Check ===\n")

    # Python packages
    print("Python Packages")
    for pkg in checks.get("python_packages", []):
        try:
            __import__(pkg.get("import_name", pkg["name"]))
            installed = version(pkg["name"])
            required = pkg.get("version")
            if required and not version_ok(installed, required):
                print(f"  FAIL  {pkg['name']} — {installed} (need {required})")
                failed += 1
            else:
                print(f"  PASS  {pkg['name']} — {installed}")
                passed += 1
        except (ImportError, PackageNotFoundError):
            print(f"  FAIL  {pkg['name']} — not installed")
            failed += 1

    # Node packages
    print("\nNode Packages")
    for pkg in checks.get("node_packages", []):
        pkg_json = REPO_ROOT / pkg["directory"] / "package.json"
        if pkg_json.exists():
            print(f"  PASS  {pkg['name']}")
            passed += 1
        else:
            print(f"  FAIL  {pkg['name']}")
            failed += 1

    # System tools
    print("\nSystem Tools")
    for tool in checks.get("system_tools", []):
        out = run(tool["command"])
        if out:
            print(f"  PASS  {tool['name']} — {out}")
            passed += 1
        else:
            print(f"  FAIL  {tool['name']}")
            failed += 1

    # Environment variables
    print("\nEnvironment Variables")
    for var in checks.get("env_variables", []):
        if os.environ.get(var["name"]):
            print(f"  PASS  {var['name']}")
            passed += 1
        else:
            print(f"  FAIL  {var['name']}")
            failed += 1

    if not checks.get("env_variables"):
        print("  (none required)")

    total = passed + failed
    print(f"\n--- {passed}/{total} checks passed ---")
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
