# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a simple Python application for generating and visualizing mathematical sequences (Fibonacci, Martingale, and Quadratic) using the `plotext` library for terminal-based plotting. The project includes PyInstaller configuration for creating standalone executables.

## Environment Setup

This project uses a Python virtual environment. To activate it:
```bash
source /home/tathienbao/python_envs/smoothenv/bin/activate
```

## Dependencies

The project has minimal dependencies:
- `plotext` (5.3.2) - for terminal-based plotting

Install dependencies:
```bash
pip install plotext
```

## Build Commands

### Building Executable
The project uses PyInstaller to create standalone executables:
```bash
# Activate virtual environment first
source /home/tathienbao/python_envs/smoothenv/bin/activate

# Build executable using the spec file
pyinstaller smooth_graph.spec
```

The built executable will be in the `dist/` directory.

### Running the Application
```bash
# Direct Python execution
python smooth_graph.py

# Or run the built executable (if available)
./dist/smooth_graph
```

## Code Architecture

### Main Application (`smooth_graph.py`)
The application is a single-file script with a simple procedural structure:

1. **User Input Phase**: Prompts user to select sequence type (1-3) and parameters
2. **Sequence Generation**: Creates mathematical sequences based on user choice:
   - Fibonacci: Recursive sequence where each term is sum of previous two
   - Martingale: Exponential doubling sequence (a₀ × 2ⁱ)
   - Quadratic: Polynomial sequence (Ai² + Bi + C)
3. **Visualization**: Uses `plotext` to render terminal-based graphs with customization

### PyInstaller Configuration (`smooth_graph.spec`)
Standard PyInstaller spec file for building standalone executables with:
- Console application mode
- UPX compression enabled
- Single-file bundle configuration

## Development Notes

- The application uses Vietnamese language prompts and labels
- No testing framework is currently configured
- No linting or code formatting tools are set up
- The codebase is intentionally simple and self-contained