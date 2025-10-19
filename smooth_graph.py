import plotext as plt

def parse_formula(formula_str):
    """
    Parse công thức từ string dạng a^2 + b*a + c
    Chuyển đổi sang Python expression: a**2 + b*a + c
    """
    # Thay thế ^ bằng **
    formula = formula_str.replace('^', '**')
    return formula

def evaluate_formula(formula, x_value):
    """Tính giá trị của công thức tại điểm x"""
    try:
        # Cho phép dùng biến x hoặc a
        result = eval(formula, {"__builtins__": {}}, {"x": x_value, "a": x_value, "i": x_value})
        return float(result)
    except:
        return None

# Main program
print("=" * 60)
print("LOT SIZING CALCULATOR - TRADING STRATEGY")
print("=" * 60)

print("\nChọn loại công thức lot sizing:")
print("1) Fibonacci - Tăng mạnh (a₀, a₁, a₀+a₁, ...)")
print("2) Martingale - Tăng cực mạnh (a₀ × 2ⁿ)")
print("3) Quadratic - Tăng vừa phải (Ax² + Bx + C)")
print("4) Custom Formula - Tự định nghĩa công thức")

choice = input("\nLựa chọn (1-4): ")
n = int(input("Số lệnh trong chuỗi (khuyến nghị 20-50): "))

seq = []

if choice == "1":
    # Fibonacci
    a0 = float(input("Lot đầu tiên (a0): "))
    a1 = float(input("Lot thứ hai (a1): "))
    seq = [a0, a1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])

elif choice == "2":
    # Martingale
    a0 = float(input("Lot ban đầu (a0): "))
    seq = [a0 * (2 ** i) for i in range(n)]

elif choice == "3":
    # Quadratic
    print("\nCông thức: y = A×x² + B×x + C")
    print("Trong đó x là thứ tự lệnh (0, 1, 2, ...)")
    A = float(input("Hệ số A (ví dụ: 0.1): "))
    B = float(input("Hệ số B (ví dụ: 0.5): "))
    C = float(input("Hệ số C (lot tối thiểu, ví dụ: 0.01): "))
    seq = [A*i*i + B*i + C for i in range(n)]

elif choice == "4":
    # Custom Formula
    print("\n" + "=" * 60)
    print("CUSTOM FORMULA")
    print("=" * 60)
    print("\nHướng dẫn nhập công thức:")
    print("  - Biến: sử dụng 'x' hoặc 'a' hoặc 'i' (thứ tự lệnh: 0, 1, 2, ...)")
    print("  - Lũy thừa: dùng ^ hoặc ** (ví dụ: x^2 hoặc x**2)")
    print("  - Phép toán: +, -, *, /")
    print("\nVí dụ công thức:")
    print("  - 0.01 + 0.02*x          → Tăng tuyến tính")
    print("  - 0.01*x^2 + 0.05*x + 0.01 → Tăng theo bậc 2")
    print("  - 0.01*(1.5^x)           → Tăng hàm mũ (chậm hơn Martingale)")
    print("  - 0.01 + 0.001*x^3       → Tăng theo bậc 3")

    formula = input("\nNhập công thức: ")
    formula_python = parse_formula(formula)

    print(f"\nCông thức đã parse: {formula_python}")
    confirm = input("Tiếp tục? (y/n): ")

    if confirm.lower() != 'y':
        print("Đã hủy!")
        exit()

    # Generate sequence
    for i in range(n):
        value = evaluate_formula(formula_python, i)
        if value is None:
            print(f"Lỗi: Không thể tính giá trị tại x={i}")
            exit()
        seq.append(value)

else:
    print("Lựa chọn không hợp lệ")
    exit()

# Display statistics
print("\n" + "=" * 60)
print("KẾT QUẢ LOT SIZING")
print("=" * 60)
print(f"Tổng số lệnh: {len(seq)}")
print(f"Lot đầu tiên: {seq[0]:.4f}")
print(f"Lot cuối cùng: {seq[-1]:.4f}")
print(f"Tổng lot toàn bộ chuỗi: {sum(seq):.4f}")
print(f"Lot trung bình: {sum(seq)/len(seq):.4f}")

# Show first 10 and last 10 lots
print(f"\n10 lot đầu tiên:")
for i in range(min(10, len(seq))):
    print(f"  Lệnh #{i}: {seq[i]:.4f}")

if len(seq) > 10:
    print(f"\n10 lot cuối cùng:")
    for i in range(max(10, len(seq)-10), len(seq)):
        print(f"  Lệnh #{i}: {seq[i]:.4f}")

# Visualization
plt.plot(range(len(seq)), seq, marker='dot', color='cyan')

title_map = {
    "1": "Lot Sizing: Fibonacci",
    "2": "Lot Sizing: Martingale",
    "3": "Lot Sizing: Quadratic",
    "4": f"Lot Sizing: Custom ({formula if choice == '4' else ''})"
}

plt.title(title_map.get(choice, "Lot Sizing"))
plt.xlabel("Thứ tự lệnh (x)")
plt.ylabel("Kích thước Lot (y)")
plt.grid(True)
plt.show()
