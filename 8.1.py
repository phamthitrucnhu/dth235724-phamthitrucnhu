from tkinter import *

# Tạo cửa sổ giao diện
root = Tk()
root.title("Giải Phương Trình Bậc 1 - facebook.com/duythanhcse")
root.minsize(height=130, width=300)
root.resizable(height=True, width=True)

# Biến chuỗi lưu giá trị nhập vào và kết quả
stringHSA = StringVar()
stringHSB = StringVar()
stringKQ = StringVar()

# Hàm xử lý nút "Giải"
def giaiAction():
    try:
        a = float(stringHSA.get())
        b = float(stringHSB.get())
        if a == 0 and b == 0:
            stringKQ.set("Vô số nghiệm")
        elif a == 0 and b != 0:
            stringKQ.set("Vô nghiệm")
        else:
            x = -b / a
            stringKQ.set("x = " + str(x))
    except ValueError:
        stringKQ.set("Vui lòng nhập số hợp lệ")

# Hàm xử lý nút "Tiếp"
def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringKQ.set("")

# Giao diện
Label(root, text="Phương Trình Bậc 1", fg="red", font=("tahoma", 16), justify=CENTER).grid(row=0, columnspan=2)

Label(root, text="Hệ số a:").grid(row=1, column=0)
Entry(root, width=30, textvariable=stringHSA).grid(row=1, column=1)

Label(root, text="Hệ số b:").grid(row=2, column=0)
Entry(root, width=30, textvariable=stringHSB).grid(row=2, column=1)

# Các nút chức năng
frameButton = Frame(root)
Button(frameButton, text="Giải", command=giaiAction).pack(side=LEFT)
Button(frameButton, text="Tiếp", command=tiepAction).pack(side=LEFT)
Button(frameButton, text="Thoát", command=root.quit).pack(side=LEFT)
frameButton.grid(row=3, columnspan=2)

# Kết quả
Label(root, text="Kết quả:").grid(row=4, column=0)
Entry(root, width=30, textvariable=stringKQ).grid(row=4, column=1)

# Vòng lặp chính
root.mainloop()
