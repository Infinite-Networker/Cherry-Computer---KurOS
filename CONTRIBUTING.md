# Contributing to Cherry Computer — KurOS

Thank you for your interest in contributing! 🍒  
All contributions — bug reports, feature requests, documentation improvements, and code — are welcome.

---

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Reporting Bugs](#reporting-bugs)
3. [Suggesting Features](#suggesting-features)
4. [Development Setup](#development-setup)
5. [Pull Request Process](#pull-request-process)
6. [Coding Standards](#coding-standards)
7. [Commit Message Format](#commit-message-format)

---

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).  
By participating you agree to uphold a welcoming, respectful environment for everyone.

---

## Reporting Bugs

1. Search [existing issues](https://github.com/Infinite-Networker/Cherry-Computer---KurOS/issues) first.
2. If none matches, [open a new issue](https://github.com/Infinite-Networker/Cherry-Computer---KurOS/issues/new) and include:
   - Your OS and Python version
   - The `textual` and `rich` versions (`pip show textual rich`)
   - A minimal reproduction script or step-by-step description
   - The full traceback / error message

---

## Suggesting Features

Open a [feature request issue](https://github.com/Infinite-Networker/Cherry-Computer---KurOS/issues/new) and describe:
- The problem you are trying to solve
- Your proposed solution
- Any alternatives you considered

---

## Development Setup

```bash
# 1. Fork and clone
git clone https://github.com/<your-fork>/Cherry-Computer---KurOS.git
cd Cherry-Computer---KurOS

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install in editable mode
pip install -e ".[dev]"

# 4. Verify the install
python -c "from kuros.app import KurOS; print('OK')"
```

---

## Pull Request Process

1. **Branch** — create a feature branch from `main`:
   ```bash
   git checkout -b feat/my-feature
   ```
2. **Implement** your changes with tests where applicable.
3. **Lint** your code (see [Coding Standards](#coding-standards)).
4. **Commit** following the [Commit Message Format](#commit-message-format).
5. **Push** and open a Pull Request against `main`.
6. Ensure the CI checks pass.
7. A maintainer will review and merge.

---

## Coding Standards

- Code is formatted with **[Black](https://black.readthedocs.io/)** (`black .`).
- Imports are sorted with **[isort](https://pycqa.github.io/isort/)** (`isort .`).
- Type hints are encouraged for all public functions.
- Docstrings follow the **Google style**.

---

## Commit Message Format

This project uses [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(scope): short description

Optional longer body.

Optional footer (e.g. Closes #42).
```

**Types:** `feat` · `fix` · `docs` · `style` · `refactor` · `test` · `chore`

**Examples:**
```
feat(app): add CPU usage widget
fix(app): correct dark mode toggle for Textual v8
docs(readme): add screenshot section
chore(deps): bump textual to 0.50.0
```
