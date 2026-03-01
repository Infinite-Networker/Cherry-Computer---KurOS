<div align="center">

# 🍒 Cherry Computer — KurOS

**A retro terminal OS interface for the modern command line.**

[![PyPI version](https://img.shields.io/pypi/v/cherry-computer-kuros?color=ff6b6b&logo=pypi&logoColor=white)](https://pypi.org/project/cherry-computer-kuros/)
[![Python](https://img.shields.io/pypi/pyversions/cherry-computer-kuros?color=ff6b6b&logo=python&logoColor=white)](https://pypi.org/project/cherry-computer-kuros/)
[![License: MIT](https://img.shields.io/badge/License-MIT-ff6b6b.svg)](LICENSE)
[![CI](https://github.com/Infinite-Networker/Cherry-Computer---KurOS/actions/workflows/ci.yml/badge.svg)](https://github.com/Infinite-Networker/Cherry-Computer---KurOS/actions/workflows/ci.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

*Toggle dark mode · Monitor system status · Experience Cherry Computer right in your terminal.*

</div>

---

## ✨ Features

| Feature | Description |
|---|---|
| 🌓 **Dark / Light mode** | Toggle themes instantly with `d` |
| 🕐 **Live clock** | Always-on clock in the header |
| 📋 **System status** | Real-time status bar showing system health |
| 📝 **Log viewer** | Dedicated System Logs panel |
| 🌐 **Network panel** | Network Traffic monitor panel |
| ⌨️ **Keyboard-first** | Every action reachable without a mouse |
| 🎨 **Retro aesthetic** | Cherry-red accents on a sleek dark canvas |

---

## 🚀 Quick Start

### Install from PyPI

```bash
pip install cherry-computer-kuros
```

Then launch with:

```bash
kuros
```

### Run from source

```bash
# Clone the repository
git clone https://github.com/Infinite-Networker/Cherry-Computer---KurOS.git
cd Cherry-Computer---KurOS

# Install dependencies
pip install textual rich

# Run
python main.py
```

---

## ⌨️ Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `d` | Toggle dark / light mode |
| `q` | Shutdown KurOS |
| `Ctrl+C` | Emergency shutdown |

---

## 🗂️ Project Structure

```
Cherry-Computer---KurOS/
├── main.py                  # Top-level entry point (for running from source)
├── setup.py                 # Package configuration
├── pyproject.toml           # Modern build configuration
├── LICENSE                  # MIT License
├── CHANGELOG.md             # Version history
├── CONTRIBUTING.md          # Contribution guide
├── docs/
│   └── DESIGN.md            # Architecture & design decisions
└── src/
    └── kuros/
        ├── __init__.py
        └── app.py           # Main Textual application
```

---

## 🛠️ Development Setup

```bash
# Clone
git clone https://github.com/Infinite-Networker/Cherry-Computer---KurOS.git
cd Cherry-Computer---KurOS

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# Run
python main.py
```

---

## 🎨 Color Scheme

### Dark Mode
| Role | Hex |
|------|-----|
| Background | `#1a1b26` |
| Text | `#a9b1d6` |
| Accent | `#ff6b6b` |
| Surface | `#24283b` |

### Light Mode
| Role | Hex |
|------|-----|
| Background | `#f8f9fa` |
| Text | `#343a40` |
| Accent | `#dc3545` |
| Surface | `#e9ecef` |

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to open issues, submit pull requests, and follow the project's coding standards.

---

## 📋 Changelog

See [CHANGELOG.md](CHANGELOG.md) for the full version history.

---

## 📄 License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

<div align="center">

Made with ❤️ by **Cherry Computer**

</div>
