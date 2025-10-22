from tkinter import *

# Hàm cộng
def congAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        stringKQ.set(a + b)
    except ValueError:
        stringKQ.set("Lỗi nhập số")

# Hàm trừ
def truAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        stringKQ.set(a - b)
    except ValueError:
        stringKQ.set("Lỗi nhập số")

# Hàm nhân
def nhanAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        stringKQ.set(a * b)
    except ValueError:
        stringKQ.set("Lỗi nhập số")

# Hàm chia
def chiaAction():
    try:
        a = float(stringA.get())
        b = float(stringB.get())
        if b == 0:
            stringKQ.set("Không chia được cho 0")
        else:
            stringKQ.set(a / b)
    except ValueError:
        stringKQ.set("Lỗi nhập số")

# Giao diện
root = Tk()
root.title("Máy tính 4 phép toán")
root.minsize(height=150, width=300)

# Khai báo biến
stringA = StringVar()
stringB = StringVar()
stringKQ = StringVar()

# Tiêu đề
Label(root, text="Cộng Trừ Nhân Chia", fg="blue", font=("tahoma", 16)).grid(row=0, columnspan=3, pady=10)

# Frame chứa các nút
frameButton = Frame(root)
frameButton.grid(row=1, column=0, rowspan=4, padx=10)

Button(frameButton, text="Cộng", width=10, command=congAction).pack(pady=2)
Button(frameButton, text="Trừ", width=10, command=truAction).pack(pady=2)
Button(frameButton, text="Nhân", width=10, command=nhanAction).pack(pady=2)
Button(frameButton, text="Chia", width=10, command=chiaAction).pack(pady=2)

# Nhập và hiển thị kết quả
Label(root, text="Số a:").grid(row=1, column=1, sticky=W)
Entry(root, width=15, textvariable=stringA).grid(row=1, column=2)

Label(root, text="Số b:").grid(row=2, column=1, sticky=W)
Entry(root, width=15, textvariable=stringB).grid(row=2, column=2)

Label(root, text="Kết quả:").grid(row=3, column=1, sticky=W)
Entry(root, width=15, textvariable=stringKQ).grid(row=3, column=2)

# Nút thoát
Button(root, text="Thoát", command=root.quit).grid(row=4, column=2, pady=10)

# Chạy chương trình
root.mainloop()
