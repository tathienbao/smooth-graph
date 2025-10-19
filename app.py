from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def generate_fibonacci(a0, a1, n):
    """Generate Fibonacci sequence"""
    seq = [a0, a1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

def generate_martingale(a0, n):
    """Generate Martingale sequence"""
    return [a0 * (2 ** i) for i in range(n)]

def generate_quadratic(a, b, c, n):
    """Generate Quadratic sequence"""
    return [a*i*i + b*i + c for i in range(n)]

def parse_formula(formula_str):
    """Parse công thức từ string dạng a^2 + b*a + c"""
    formula = formula_str.replace('^', '**')
    return formula

def evaluate_formula(formula, x_value):
    """Tính giá trị của công thức tại điểm x"""
    try:
        result = eval(formula, {"__builtins__": {}}, {"x": x_value, "a": x_value, "i": x_value})
        return float(result)
    except:
        return None

def generate_custom(formula, n, start_value=0):
    """Generate sequence from custom formula"""
    formula_python = parse_formula(formula)
    sequence = []
    for i in range(start_value, start_value + n):
        value = evaluate_formula(formula_python, i)
        if value is None:
            raise ValueError(f"Cannot evaluate formula at x={i}")
        sequence.append(value)
    return sequence

def parse_manual_input(input_str):
    """Parse manual input string separated by semicolon"""
    try:
        numbers = [float(x.strip()) for x in input_str.split(';') if x.strip()]
        if len(numbers) < 2:
            raise ValueError("Cần ít nhất 2 số")
        return numbers
    except ValueError as e:
        raise ValueError(f"Dữ liệu không hợp lệ: {str(e)}")

def simple_moving_average(data, window=5):
    """Calculate Simple Moving Average"""
    if len(data) < window:
        window = len(data)
    last_values = data[-window:]
    return sum(last_values) / len(last_values)

def exponential_moving_average(data, alpha=0.3):
    """Calculate Exponential Moving Average"""
    ema = data[0]
    for value in data[1:]:
        ema = alpha * value + (1 - alpha) * ema

    if len(data) > 1:
        trend = data[-1] - data[-2]
        prediction = ema + trend * 0.5
    else:
        prediction = ema
    return prediction

def linear_regression_predict(data):
    """Predict next value using Linear Regression"""
    n = len(data)
    x = list(range(n))
    y = data

    x_mean = sum(x) / n
    y_mean = sum(y) / n

    numerator = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
    denominator = sum((x[i] - x_mean) ** 2 for i in range(n))

    if denominator == 0:
        return y_mean

    a = numerator / denominator
    b = y_mean - a * x_mean

    prediction = a * n + b
    return prediction

def polynomial_regression_predict(data, degree=2):
    """Predict next value using Polynomial Regression"""
    n = len(data)

    if degree == 2 and n >= 3:
        x0, x1, x2 = n-3, n-2, n-1
        y0, y1, y2 = data[x0], data[x1], data[x2]

        denom = (x0 - x1) * (x0 - x2) * (x1 - x2)
        if denom != 0:
            a = (x2*(y1-y0) + x1*(y0-y2) + x0*(y2-y1)) / denom
            b = (x2**2*(y0-y1) + x1**2*(y2-y0) + x0**2*(y1-y2)) / denom
            c = (x1*x2*(x1-x2)*y0 + x2*x0*(x2-x0)*y1 + x0*x1*(x0-x1)*y2) / denom

            prediction = a * n**2 + b * n + c
            return prediction

    return linear_regression_predict(data)

def predict_next_values(data, method, count=10):
    """Predict next 'count' values using specified method"""
    predictions = []
    current_data = data[:]

    for _ in range(count):
        if method == 'sma':
            pred = simple_moving_average(current_data)
        elif method == 'ema':
            pred = exponential_moving_average(current_data)
        elif method == 'linear':
            pred = linear_regression_predict(current_data)
        elif method == 'poly2':
            pred = polynomial_regression_predict(current_data, degree=2)
        else:
            pred = current_data[-1]

        predictions.append(pred)
        current_data.append(pred)

    return predictions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare-all', methods=['POST'])
def compare_all():
    """Generate all curves for comparison"""
    try:
        data = request.get_json()
        n = int(data.get('n', 50))
        start_value = int(data.get('start_value', 0))

        results = {}

        # Fibonacci
        if data.get('enable_fibonacci', True):
            fib_a0 = float(data.get('fib_a0', 1))
            fib_a1 = float(data.get('fib_a1', 1))
            results['fibonacci'] = generate_fibonacci(fib_a0, fib_a1, n)

        # Martingale
        if data.get('enable_martingale', True):
            mart_a0 = float(data.get('mart_a0', 0.01))
            results['martingale'] = generate_martingale(mart_a0, n)

        # Quadratic
        if data.get('enable_quadratic', True):
            quad_a = float(data.get('quad_a', 0.01))
            quad_b = float(data.get('quad_b', 0.02))
            quad_c = float(data.get('quad_c', 0.01))
            results['quadratic'] = generate_quadratic(quad_a, quad_b, quad_c, n)

        # Custom formulas (up to 3)
        for i in range(1, 4):
            formula_key = f'custom_formula_{i}'
            if data.get(f'enable_custom_{i}', False) and data.get(formula_key):
                formula = data[formula_key]
                results[f'custom_{i}'] = generate_custom(formula, n, start_value)

        # Manual data
        manual_data = None
        if data.get('enable_manual', False) and data.get('manual_input'):
            manual_data = parse_manual_input(data['manual_input'])
            results['manual'] = manual_data

        # Predictions from manual data
        if manual_data and data.get('enable_predictions', False):
            predict_count = int(data.get('predict_count', 10))

            if data.get('enable_linear_pred', True):
                results['pred_linear'] = predict_next_values(manual_data, 'linear', predict_count)

            if data.get('enable_poly2_pred', True):
                results['pred_poly2'] = predict_next_values(manual_data, 'poly2', predict_count)

            if data.get('enable_sma_pred', True):
                results['pred_sma'] = predict_next_values(manual_data, 'sma', predict_count)

            if data.get('enable_ema_pred', True):
                results['pred_ema'] = predict_next_values(manual_data, 'ema', predict_count)

        # Calculate metrics for each curve
        metrics = {}
        for name, sequence in results.items():
            if sequence and not name.startswith('pred_'):
                metrics[name] = {
                    'first': sequence[0],
                    'last': sequence[-1],
                    'total': sum(sequence),
                    'average': sum(sequence) / len(sequence),
                    'count': len(sequence),
                    'growth_rate': (sequence[-1] - sequence[0]) / sequence[0] * 100 if sequence[0] != 0 else 0
                }

        return jsonify({
            'curves': results,
            'metrics': metrics,
            'indices': list(range(n)),
            'prediction_indices': list(range(n, n + data.get('predict_count', 10))) if manual_data else []
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/generate', methods=['POST'])
def generate_sequence():
    try:
        data = request.get_json()
        sequence_type = data['type']
        n = int(data['n'])

        if sequence_type == 'fibonacci':
            a0 = float(data['a0'])
            a1 = float(data['a1'])
            sequence = generate_fibonacci(a0, a1, n)
        elif sequence_type == 'martingale':
            a0 = float(data['a0'])
            sequence = generate_martingale(a0, n)
        elif sequence_type == 'quadratic':
            a = float(data['a'])
            b = float(data['b'])
            c = float(data['c'])
            sequence = generate_quadratic(a, b, c, n)
        elif sequence_type == 'custom':
            formula = data['formula']
            start_value = int(data.get('start_value', 0))
            sequence = generate_custom(formula, n, start_value)
        elif sequence_type == 'manual':
            input_str = data['manual_input']
            historical_data = parse_manual_input(input_str)

            # Get prediction parameters
            predict_method = data.get('predict_method', 'none')
            predict_count = int(data.get('predict_count', 10))

            if predict_method != 'none':
                # Generate predictions
                predictions = predict_next_values(historical_data, predict_method, predict_count)
                sequence = historical_data

                # Calculate statistics
                total_lot = sum(sequence)
                avg_lot = total_lot / len(sequence)

                return jsonify({
                    'sequence': sequence,
                    'predictions': predictions,
                    'indices': list(range(len(sequence))),
                    'prediction_indices': list(range(len(sequence), len(sequence) + len(predictions))),
                    'stats': {
                        'total': total_lot,
                        'average': avg_lot,
                        'first': sequence[0],
                        'last': sequence[-1],
                        'count': len(sequence),
                        'predicted_next': predictions[0] if predictions else None
                    }
                })
            else:
                sequence = historical_data
        else:
            return jsonify({'error': 'Invalid sequence type'}), 400

        # Calculate statistics
        total_lot = sum(sequence)
        avg_lot = total_lot / len(sequence)

        return jsonify({
            'sequence': sequence,
            'indices': list(range(len(sequence))),
            'stats': {
                'total': total_lot,
                'average': avg_lot,
                'first': sequence[0],
                'last': sequence[-1],
                'count': len(sequence)
            }
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Vercel entry point
app = app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)