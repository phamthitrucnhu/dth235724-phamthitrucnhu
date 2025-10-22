from tkinter import *

root = Tk()
root.title("Phần mềm tính BMI")
root.geometry("350x300")
root.configure(bg="yellow")

# Nhãn nhập liệu
Label(root, text="Nhập chiều cao (m):", bg="yellow", font=('Arial', 11)).grid(row=0, column=0, padx=10, pady=10)
entry_height = Entry(root, width=10)
entry_height.grid(row=0, column=1)

Label(root, text="Nhập cân nặng (kg):", bg="yellow", font=('Arial', 11)).grid(row=1, column=0, padx=10, pady=10)
entry_weight = Entry(root, width=10)
entry_weight.grid(row=1, column=1)

# Kết quả hiển thị
Label(root, text="BMI của bạn:", bg="yellow", font=('Arial', 11)).grid(row=3, column=0, padx=10, pady=10)
bmi_value = StringVar()
Label(root, textvariable=bmi_value, bg="yellow", font=('Arial', 11, 'bold')).grid(row=3, column=1)

Label(root, text="Tình trạng của bạn:", bg="yellow", font=('Arial', 11)).grid(row=4, column=0, padx=10, pady=10)
status = StringVar()
Label(root, textvariable=status, bg="yellow", font=('Arial', 11, 'bold')).grid(row=4, column=1)

Label(root, text="Nguy cơ phát triển bệnh:", bg="yellow", font=('Arial', 11)).grid(row=5, column=0, padx=10, pady=10)
risk = StringVar()
Label(root, textvariable=risk, bg="yellow", font=('Arial', 11, 'bold')).grid(row=5, column=1)


# Hàm tính BMI
def tinh_bmi():
    try:
        h = float(entry_height.get())
        w = float(entry_weight.get())
        bmi = w / (h * h)
        bmi_value.set(f"{bmi:.2f}")

        if bmi < 18.5:
            status.set("Gầy")
            risk.set("Thấp")
        elif bmi < 25:
            status.set("Bình thường")
            risk.set("Trung bình")
        elif bmi < 30:
            status.set("Hơi béo")
            risk.set("Hơi cao")
        else:
            status.set("Béo phì")
            risk.set("Rất cao")
    except:
        bmi_value.set("Lỗi")
        status.set("")
        risk.set("")


# Nút tính và thoát
Button(root, text="Tính BMI", command=tinh_bmi, bg="lightblue").grid(row=2, column=1, pady=10)
Button(root, text="Thoát", command=root.quit, bg="orange").grid(row=6, column=1, pady=15)

root.mainloop()
