# Troubleshooting Dependency Checks

Fixes for each failure type reported by this skill.

## Python Packages

**FAIL — package not installed**

```bash
python3 -m pip install <package-name>
```

Or install everything in the lock file:

```bash
python3 -m pip install -r requirements.txt
```

**FAIL — version mismatch (`X.Y.Z` installed, need `>=A.B`)**

Upgrade to the required version:

```bash
python3 -m pip install "<package-name>>=<version>"
```

Note: if pip reports `externally-managed-environment`, use
`pip install --break-system-packages` or a virtual environment:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

## Node Packages

**FAIL — package not installed or incomplete**

```bash
cd .opencode && npm install
```

If the package directory exists but `package.json` is missing, delete it and
reinstall:

```bash
rm -rf node_modules
npm install
```

## System Tools

**FAIL — python3 missing**

- Debian/Ubuntu: `sudo apt install python3`
- macOS (Homebrew): `brew install python3`
- Windows: install from https://python.org

**FAIL — git missing**

- Debian/Ubuntu: `sudo apt install git`
- macOS (Homebrew): `brew install git`
- Windows: install from https://git-scm.com

**FAIL — node missing**

- Debian/Ubuntu: `sudo apt install nodejs npm`
- macOS (Homebrew): `brew install node`
- Windows: install from https://nodejs.org

## Environment Variables

**FAIL — variable not set**

```bash
export VARIABLE_NAME="value"
```

For persistence, add the line to your shell profile (`~/.bashrc`,
`~/.zshrc`) or use a `.env` file loaded by your environment.