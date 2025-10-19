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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_sequence():
    try:
        data = request.get_json()
        sequence_type = data['type']
        n = int(data['n'])
        
        if sequence_type == 'fibonacci':
            a0 = int(data['a0'])
            a1 = int(data['a1'])
            sequence = generate_fibonacci(a0, a1, n)
        elif sequence_type == 'martingale':
            a0 = float(data['a0'])
            sequence = generate_martingale(a0, n)
        elif sequence_type == 'quadratic':
            a = float(data['a'])
            b = float(data['b'])
            c = float(data['c'])
            sequence = generate_quadratic(a, b, c, n)
        else:
            return jsonify({'error': 'Invalid sequence type'}), 400
        
        return jsonify({
            'sequence': sequence,
            'indices': list(range(len(sequence)))
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)