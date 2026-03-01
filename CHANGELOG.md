# Changelog

All notable changes to **Cherry Computer — KurOS** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.4] — 2026-03-01

### Added
- `src/__init__.py` and `src/kuros/__init__.py` — package marker files so
  `setuptools.find_packages` correctly discovers the `kuros` package and
  `from kuros.app import KurOS` works in all environments.
- `kuros.app.main()` module-level entry-point function so the installed
  `kuros` command-line script works after `pip install`.
- `pyproject.toml` — modern PEP 517/518 build configuration alongside
  `setup.py` for compatibility with the latest packaging tooling.
- `CHANGELOG.md` — this file.
- `CONTRIBUTING.md` — contributor guidelines.
- GitHub Actions CI workflow (`.github/workflows/ci.yml`) — runs lint and
  import checks on Python 3.9 through 3.12 on every push and pull request.
- GitHub Actions PyPI publish workflow (`.github/workflows/publish.yml`) —
  automatically builds and uploads the distribution to PyPI when a `v*` tag
  is pushed.

### Fixed
- **`App.dark` removed in Textual ≥ 0.45** — `action_toggle_dark` previously
  set `self.dark = not self.dark` which raises `AttributeError` on Textual v8.
  It now uses `self.theme` toggling between `"textual-dark"` and
  `"textual-light"`.
- **Broken `console_scripts` entry point** — `"kuros=main:main"` referenced the
  top-level `main.py` which is not part of the installed package; corrected to
  `"kuros=kuros.app:main"`.
- **Placeholder project URL** — `setup.py` contained `yourusername/cherry-computer-kuros`;
  updated to the real repository URL.
- **Unbounded `textual` dependency** — pinned upper bound to `<9.0.0` to guard
  against future breaking major releases.

---

## [1.0.3] — initial release

### Added
- Initial KurOS terminal application built on the [Textual](https://github.com/Textualize/textual) framework.
- Header with live clock.
- Dark / light mode toggle (`d`).
- System status bar.
- System Logs and Network Traffic placeholder panels.
- Keyboard shortcuts: `d` (theme), `q` (quit), `Ctrl+C` (emergency quit).
