# Smooth Graph

A web-based tool for generating mathematical sequences and analyzing price data. Includes both a Flask web interface and terminal CLI.

## Features

### Sequence Generation
- **Fibonacci**: Generate Fibonacci sequences with custom starting values
- **Martingale**: Exponential doubling sequence (a₀ × 2ⁿ)
- **Quadratic**: Polynomial sequences (Ax² + Bx + C)
- **Custom Formula**: User-defined mathematical formulas with customizable start value

### Price Analysis
- **Manual Data Input**: Import price data (semicolon-separated)
- **Prediction Methods**:
  - Linear Regression
  - Polynomial Regression (degree 2)
  - Simple Moving Average (SMA)
  - Exponential Moving Average (EMA)
- **Visualization**: Historical data (solid line) + predictions (dashed line)

### Comparison Mode
- Compare multiple curves simultaneously on one chart
- Toggle individual curves on/off via legend
- Metrics table showing first/last values, totals, averages, and growth rates
- Support for up to:
  - 3 standard formulas (Fibonacci, Martingale, Quadratic)
  - 3 custom formulas
  - 1 manual data set
  - 4 prediction methods

## Installation

```bash
git clone <repo-url>
cd smoothenv
python -m venv .
source bin/activate  # Windows: .\Scripts\activate
pip install Flask plotext
```

## Usage

### Web Interface
```bash
python app.py
```
Open http://localhost:5000

### Terminal CLI
```bash
python smooth_graph.py
```

## Formula Syntax

Variables: `x`, `a`, or `i` (index position)
Operations: `+`, `-`, `*`, `/`
Power: `^` or `**`

Examples:
```
0.01 + 0.02*x              # Linear
0.01*x^2 + 0.05*x + 0.01   # Quadratic
0.01*(1.5^x)               # Exponential
5 + 2*x + 0.3*x^2          # Parabola
```

Start value controls where x begins:
- Start = 0: x goes 0, 1, 2, 3, ...
- Start = 5: x goes 5, 6, 7, 8, ...

## Data Format

Manual input uses semicolon separator:
```
100;102;105;103;108;110
```

## Prediction Algorithms

**Linear Regression**: Least squares fitting (y = ax + b)
**Polynomial (degree 2)**: Parabolic fitting via 3-point method
**SMA**: Average of last 5 values
**EMA**: Exponential weighting (alpha = 0.3)

## Project Structure

```
smoothenv/
├── app.py              # Flask backend
├── smooth_graph.py     # Terminal version
├── templates/
│   └── index.html      # Web UI
└── README.md
```

## Deployment

### Vercel
```bash
npm i -g vercel
vercel
```

### Heroku
```bash
pip freeze > requirements.txt
echo "web: python app.py" > Procfile
git push heroku master
```

## License

MIT
