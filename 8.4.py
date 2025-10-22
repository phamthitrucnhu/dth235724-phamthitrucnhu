from tkinter import *

# Tạo cửa sổ chính
root = Tk()
root.title("Máy tính bỏ túi")
root.geometry("300x400")

# Biến lưu biểu thức
expression = ""

# Hàm hiển thị lên ô nhập
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

# Hàm tính kết quả
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Lỗi")
        expression = ""

# Hàm xóa toàn bộ
def clear():
    global expression
    expression = ""
    equation.set("")

# Ô hiển thị
equation = StringVar()
entry_field = Entry(root, textvariable=equation, font=('Arial', 18), justify='right')
entry_field.grid(columnspan=4, ipadx=8, ipady=8, pady=10)

# Các nút số và phép toán
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

for (text, row, col) in buttons:
    if text == '=':
        Button(root, text=text, height=2, width=6, command=equalpress).grid(row=row, column=col, padx=5, pady=5)
    else:
        Button(root, text=text, height=2, width=6, command=lambda t=text: press(t)).grid(row=row, column=col, padx=5, pady=5)

# Nút Xóa
Button(root, text='Clr', height=2, width=28, command=clear).grid(row=5, columnspan=4, padx=5, pady=10)

root.mainloop()
