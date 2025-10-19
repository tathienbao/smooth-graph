# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Smooth Graph is a dual-interface Python application for:
- **Lot Sizing Strategies**: Generate and visualize position sizing for trading (Fibonacci, Martingale, Quadratic, Custom formulas)
- **Price Prediction**: Analyze historical data and predict future values using Linear Regression, Polynomial, SMA, EMA

The project includes both a web interface (Flask + Chart.js) and a terminal CLI (plotext).

## Environment Setup

This project uses a Python virtual environment. To activate it:
```bash
# Linux/Mac
source bin/activate

# Windows
.\Scripts\activate
```

If setting up from scratch:
```bash
python -m venv .
source bin/activate  # or .\Scripts\activate on Windows
pip install Flask plotext
```

## Dependencies

Core dependencies:
- `Flask` (3.1.2) - Web framework
- `plotext` (5.3.2) - Terminal-based plotting
- PyInstaller (optional) - For building executables

Install dependencies:
```bash
pip install Flask plotext
```

## Running the Application

### Web Interface (Recommended)
```bash
python app.py
```
Then open browser at: http://localhost:5000

### Terminal CLI
```bash
python smooth_graph.py
```

### Building Executable (Optional)
```bash
pyinstaller smooth_graph.spec
./dist/smooth_graph
```

## Code Architecture

### Web Application (`app.py`)
Flask backend with prediction algorithms:
- **Lot Sizing**: Fibonacci, Martingale, Quadratic, Custom formula generation
- **Price Prediction**: SMA, EMA, Linear/Polynomial regression
- **API Endpoints**:
  - `GET /` - Serve web UI
  - `POST /generate` - Generate sequences/predictions
- **Security**: Restricted eval for formula parsing

### Terminal CLI (`smooth_graph.py`)
Standalone lot sizing calculator:
- Interactive prompts for strategy selection
- Custom formula support with start value
- ASCII-based chart visualization
- Statistics display

### Web UI (`templates/index.html`)
Single-page application with:
- Chart.js for interactive visualizations
- Dynamic form handling (5 sequence types)
- Dual-line charts (historical + predicted data)
- Responsive design

## Key Features

### Lot Sizing (Trading)
1. **Fibonacci**: Progressive increase (a₀, a₁, a₀+a₁, ...)
2. **Martingale**: Exponential doubling (a₀ × 2ⁿ)
3. **Quadratic**: Polynomial growth (Ax² + Bx + C)
4. **Custom Formula**: User-defined expressions (supports ^, **, +, -, *, /)

### Price Prediction (Manual Input)
1. **Input**: Historical prices (semicolon-separated)
2. **Methods**: Linear Regression, Polynomial (degree 2), SMA, EMA
3. **Output**: Dual chart with actual (blue) + predicted (red) lines

## Custom Formula Syntax

Variables: `x`, `a`, or `i` (position/index)
Operations: `+`, `-`, `*`, `/`
Power: `^` or `**`

Examples:
- `0.01 + 0.02*x` - Linear growth
- `0.01*x^2 + 0.05*x + 0.01` - Quadratic
- `0.01*(1.5^x)` - Exponential
- `5 + 2*x + 0.3*x^2` - Smooth parabola

## Development Notes

- Vietnamese language UI/prompts
- No testing framework configured
- Security: eval() with restricted builtins
- Simple, self-contained architecture
- Stateless API design