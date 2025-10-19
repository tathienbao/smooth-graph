# 📊 Smooth Graph - Lot Sizing & Price Prediction Tool

A powerful web-based tool for generating mathematical sequences, visualizing lot sizing strategies for trading, and predicting price movements using various statistical methods.

## 🌟 Features

### 1. **Lot Sizing Strategies** (For Trading)
Generate and visualize different position sizing strategies:
- **Fibonacci**: Progressive increase based on Fibonacci sequence
- **Martingale**: Exponential doubling (aggressive)
- **Quadratic**: Polynomial growth (Ax² + Bx + C)
- **Custom Formula**: Define your own mathematical formula

### 2. **Price Prediction** (Manual Input + AI)
Analyze real price data and predict future values:
- Input historical prices (gold, stocks, crypto, etc.)
- Choose prediction method:
  - **Linear Regression**: Best for trending data
  - **Polynomial (Degree 2)**: For curved trends
  - **Simple Moving Average (SMA)**: For oscillating data
  - **Exponential Moving Average (EMA)**: Weighted recent data
- Predict 1-50 future data points
- Visualize historical vs predicted values

### 3. **Dual Interface**
- **Web UI**: Interactive charts with Chart.js
- **Terminal CLI**: Text-based visualization with plotext

---

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- pip

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd smoothenv
```

2. **Create and activate virtual environment**
```bash
python -m venv .
source bin/activate  # On Windows: .\Scripts\activate
```

3. **Install dependencies**
```bash
pip install Flask plotext
```

### Running the Application

#### Web Version (Recommended)
```bash
python app.py
```
Then open your browser at: **http://localhost:5000**

#### Terminal Version
```bash
python smooth_graph.py
```

---

## 📖 Usage Guide

### Web Interface

#### 1. Lot Sizing (Trading Strategy)
Perfect for planning position sizes in trading sequences:

**Example - Quadratic Strategy:**
- Select: "Quadratic (Bậc 2)"
- A: 0.01 (controls curve steepness)
- B: 0.02 (linear component)
- C: 0.01 (starting lot size)
- Number of orders: 50
- Result: Smooth progressive increase in lot sizes

**Example - Custom Formula:**
- Select: "Custom Formula"
- Formula: `0.01*(1.3^x)`
- Result: Exponential growth slower than Martingale

#### 2. Price Prediction
Analyze and forecast price movements:

**Example - Stock Price Analysis:**
```
Input prices (separated by ;):
2850.50;2855.20;2860.10;2858.40;2862.30;2865.80;2870.50;2868.20;2872.60;2875.40

Prediction method: Linear Regression
Prediction points: 10
```

The chart will show:
- 🔵 **Blue line (solid)**: Your actual price data
- 🔴 **Red line (dashed)**: Predicted future prices

---

## 🎯 Use Cases

### Trading & Risk Management
1. **Position Sizing**: Test different lot sizing strategies before live trading
2. **Risk Analysis**: Visualize how quickly your position grows
3. **Comparison**: Compare Fibonacci vs Martingale vs custom strategies

### Price Forecasting
1. **Technical Analysis**: Predict next price movements
2. **Trend Detection**: Identify patterns in historical data
3. **Data Visualization**: Beautiful charts for presentations

---

## 🛠️ Technical Details

### Prediction Algorithms

#### Linear Regression
- Uses least squares method
- Formula: y = ax + b
- Best for: Data with clear linear trends

#### Polynomial Regression (Degree 2)
- Uses parabolic fitting
- Formula: y = ax² + bx + c
- Best for: Data with curved trends

#### Simple Moving Average (SMA)
- Average of last N values (window = 5)
- Best for: Smoothing oscillating data

#### Exponential Moving Average (EMA)
- Weighted average favoring recent data
- Alpha = 0.3 (configurable)
- Best for: Responsive predictions

### Custom Formula Syntax
Supports standard mathematical operations:
- Variables: `x`, `a`, or `i` (position/index)
- Operations: `+`, `-`, `*`, `/`
- Power: `^` or `**`
- Parentheses: `()`

**Examples:**
```
0.01 + 0.02*x           # Linear growth
0.01*x^2 + 0.05*x + 0.01  # Quadratic
0.01*(1.5^x)            # Exponential (custom base)
0.01 + 0.001*x^3        # Cubic growth
```

---

## 📁 Project Structure

```
smoothenv/
├── app.py                  # Flask web application
├── smooth_graph.py         # Terminal CLI version
├── templates/
│   └── index.html         # Web UI (HTML + Chart.js)
├── requirements.txt        # Python dependencies (if created)
├── README.md              # This file
└── vercel.json            # Vercel deployment config
```

---

## 🌐 Deployment

### Deploy to Vercel (Free)
1. Install Vercel CLI: `npm i -g vercel`
2. Run: `vercel`
3. Follow prompts
4. Your app will be live at: `https://your-app.vercel.app`

### Deploy to Heroku
1. Create `requirements.txt`:
```bash
pip freeze > requirements.txt
```

2. Create `Procfile`:
```
web: python app.py
```

3. Deploy:
```bash
heroku create
git push heroku master
```

---

## 🎨 Screenshots

### Web Interface
- Clean, modern UI with responsive design
- Interactive charts with zoom/pan capabilities
- Real-time calculation and visualization

### Terminal Version
- ASCII-based charts
- Lightweight and fast
- Perfect for SSH/remote servers

---

## 🤝 Contributing

Contributions are welcome! Here are some ideas:
- Add more prediction algorithms (ARIMA, LSTM)
- Export data to CSV
- Save/load presets
- Multiple chart comparison
- Dark mode

---

## 📝 License

MIT License - feel free to use this project for personal or commercial purposes.

---

## 🙏 Acknowledgments

- **Flask**: Web framework
- **Chart.js**: Beautiful web charts
- **plotext**: Terminal plotting library

---

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Happy Trading & Analyzing! 📈**
