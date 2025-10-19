import plotext as plt

print("Chọn loại dãy muốn vẽ:")
print("1) Fibonacci")
print("2) Martingale")
print("3) Quadratic")

choice = input("Lựa chọn (1-3): ")
n = int(input("Số phần tử cần sinh: "))

if choice == "1":
    a0 = int(input("a0: "))
    a1 = int(input("a1: "))
    seq = [a0, a1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
elif choice == "2":
    a0 = float(input("Giá trị đầu tiên (a0): "))
    seq = [a0 * (2 ** i) for i in range(n)]
elif choice == "3":
    A = float(input("a: "))
    B = float(input("b: "))
    C = float(input("c: "))
    seq = [A*i*i + B*i + C for i in range(n)]
else:
    print("Lựa chọn không hợp lệ")
    exit()

plt.plot(range(len(seq)), seq, marker='dot', color='cyan')
plt.title("Sequence Graph")
plt.xlabel("Index (n)")
plt.ylabel("Value")
plt.grid(True)
plt.show()
