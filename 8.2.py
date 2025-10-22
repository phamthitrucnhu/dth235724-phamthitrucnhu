from tkinter import *
from math import sqrt


# Hàm giải phương trình
def giaiAction():
    try:
        a = float(stringHSA.get())
        b = float(stringHSB.get())
        c = float(stringHSC.get())

        if a == 0:  # bx + c = 0
            if b == 0 and c == 0:
                stringKQ.set("Vô số nghiệm")
            elif b == 0 and c != 0:
                stringKQ.set("Vô nghiệm")
            else:
                x = -c / b
                stringKQ.set("x = " + str(x))
        else:
            delta = b ** 2 - 4 * a * c
            if delta < 0:
                stringKQ.set("Vô nghiệm")
            elif delta == 0:
                x = -b / (2 * a)
                stringKQ.set("Nghiệm kép x1 = x2 = " + str(x))
            else:
                x1 = (-b - sqrt(delta)) / (2 * a)
                x2 = (-b + sqrt(delta)) / (2 * a)
                stringKQ.set("x1 = " + str(x1) + "; x2 = " + str(x2))
    except ValueError:
        stringKQ.set("Vui lòng nhập số hợp lệ!")


# Hàm làm mới dữ liệu
def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringHSC.set("")
    stringKQ.set("")


# Giao diện
root = Tk()
root.title("Giải Phương Trình Bậc 2")
root.minsize(height=200, width=400)

# Khai báo biến
stringHSA = StringVar()
stringHSB = StringVar()
stringHSC = StringVar()
stringKQ = StringVar()

# Tiêu đề
Label(root, text="Phương Trình Bậc 2", fg="red", font=("tahoma", 16)).grid(row=0, column=0, columnspan=2, pady=10)

# Nhập hệ số
Label(root, text="Hệ số a:").grid(row=1, column=0, sticky=W, padx=5)
Entry(root, width=30, textvariable=stringHSA).grid(row=1, column=1)

Label(root, text="Hệ số b:").grid(row=2, column=0, sticky=W, padx=5)
Entry(root, width=30, textvariable=stringHSB).grid(row=2, column=1)

Label(root, text="Hệ số c:").grid(row=3, column=0, sticky=W, padx=5)
Entry(root, width=30, textvariable=stringHSC).grid(row=3, column=1)

# Nút chức năng
frameButton = Frame(root)
frameButton.grid(row=4, column=0, columnspan=2, pady=10)

Button(frameButton, text="Giải", width=10, command=giaiAction).pack(side=LEFT, padx=5)
Button(frameButton, text="Tiếp", width=10, command=tiepAction).pack(side=LEFT, padx=5)
Button(frameButton, text="Thoát", width=10, command=root.quit).pack(side=LEFT, padx=5)

# Kết quả
Label(root, text="Kết quả:").grid(row=5, column=0, sticky=W, padx=5)
Entry(root, width=30, textvariable=stringKQ).grid(row=5, column=1)

# Chạy vòng lặp giao diện
root.mainloop()
