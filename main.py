#!/usr/bin/env python3
"""
Cherry Computer - KurOS
Main entry point for the KurOS terminal interface.
"""

from kuros.app import KurOS

def main():
    """Initialize and run the KurOS application."""
    app = KurOS()
    app.run()

if __name__ == "__main__":
    main()
