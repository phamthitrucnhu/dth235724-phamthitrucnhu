import math

a = float(input("Nhập cơ số a (> 0, a ≠ 1): "))
x = float(input("Nhập số x (> 0): "))

if a > 0 and a != 1 and x > 0:
    logax = math.log(x) / math.log(a)
    print(f"log cơ số {a} của {x} là:", round(logax, 4))
else:
    print("❌ Giá trị a hoặc x không hợp lệ.")
