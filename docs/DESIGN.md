# KurOS Design Document

## Architecture Overview

KurOS is built on the Textual framework, providing a rich terminal user interface with modern features while maintaining a retro aesthetic.

### Core Components

1. **App Layer** (`app.py`)
   - Main application controller
   - Event handling
   - Theme management

2. **Widget Layer** (`widgets/`)
   - Custom UI components
   - System status displays
   - Log viewers

3. **Data Layer** (`config.py`)
   - Configuration management
   - System state
   - User preferences

## UI/UX Design Principles

- **Retro-futuristic** - Clean lines with a nod to classic terminals
- **Keyboard-first** - All functions accessible via keyboard
- **Minimalist** - Only essential information displayed
- **Responsive** - Adapts to terminal size changes

## Color Scheme

### Dark Mode
- Background: #1a1b26
- Text: #a9b1d6
- Accent: #ff6b6b
- Surface: #24283b

### Light Mode
- Background: #f8f9fa
- Text: #343a40
- Accent: #dc3545
- Surface: #e9ecef

## Keyboard Navigation
