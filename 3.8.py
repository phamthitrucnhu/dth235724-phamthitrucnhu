# Nhập 2 số
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

# Nhập phép toán
phep_toan = input("Nhập phép toán (+, -, *, /): ")

# Tính và in kết quả
if phep_toan == '+':
    ket_qua = a + b
    print("Kết quả:", ket_qua)
elif phep_toan == '-':
    ket_qua = a - b
    print("Kết quả:", ket_qua)
elif phep_toan == '*':
    ket_qua = a * b
    print("Kết quả:", ket_qua)
elif phep_toan == '/':
    if b == 0:
        print("Lỗi: Không thể chia cho 0.")
    else:
        ket_qua = a / b
        print("Kết quả:", ket_qua)
else:
    print("Phép toán không hợp lệ. Vui lòng nhập +, -, *, hoặc /.")
