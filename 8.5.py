from tkinter import *

root = Tk()
root.title("Màn hình đăng nhập")
root.geometry("300x200")

Label(root, text="mật khẩu cũ:").grid(row=0, column=0, padx=10, pady=10)
username = Entry(root, width=25)
username.grid(row=0, column=1)

Label(root, text="Mật khẩu mới:").grid(row=1, column=0, padx=10, pady=10)
password = Entry(root, width=25, show="*")
password.grid(row=1, column=1)
Label(root, text=" nhập lại Mật khẩu:").grid(row=3, column=0, padx=10, pady=10)
password = Entry(root, width=25, show="*")
password.grid(row=3, column=1)

def login():
    user = username.get()
    pwd = password.get()
    if user == "admin" and pwd == "123":
        result.set("Đăng nhập thành công!")
    else:
        result.set("Sai tài khoản hoặc mật khẩu!")

def exit_app():
    root.quit()

Button(root, text="Đăng nhập", command=login).grid(row=4, column=0, pady=10)
Button(root, text="Thoát", command=exit_app).grid(row=4, column=1, pady=10)

result = StringVar()
Label(root, textvariable=result, fg="blue").grid(row=3, columnspan=2)

root.mainloop()
