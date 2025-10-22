from tkinter import *

root = Tk()
root.title("Chuyển độ F sang độ C")
root.geometry("300x200")
root.configure(bg="yellow")

# Nhãn và ô nhập
Label(root, text="Nhập độ F:", bg="yellow", font=('Arial', 11)).grid(row=0, column=0, padx=10, pady=10)
entry_f = Entry(root, width=10)
entry_f.grid(row=0, column=1)

Label(root, text="Độ C:", bg="yellow", font=('Arial', 11)).grid(row=2, column=0, padx=10, pady=10)
result = StringVar()
Label(root, textvariable=result, bg="yellow", font=('Arial', 11, 'bold')).grid(row=2, column=1)

# Hàm chuyển đổi
def convert():
    try:
        f = float(entry_f.get())
        c = (f - 32) * 5 / 9
        result.set(f"{c:.2f} °C")
    except:
        result.set("Lỗi nhập liệu!")

# Nút chuyển
Button(root, text="Chuyển", command=convert, bg="lightblue").grid(row=1, column=1, pady=10)

root.mainloop()
