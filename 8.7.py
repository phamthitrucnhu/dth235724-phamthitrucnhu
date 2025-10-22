from tkinter import *

root = Tk()
root.title("Chuyển năm Dương lịch sang Âm lịch")
root.geometry("350x200")

Label(root, text="Nhập năm dương:", font=('Arial', 11)).grid(row=0, column=0, padx=10, pady=10)
nam_duong = Entry(root, width=10)
nam_duong.grid(row=0, column=1)

Label(root, text="Năm âm:", font=('Arial', 11)).grid(row=2, column=0, padx=10, pady=10)
ketqua = StringVar()
Label(root, textvariable=ketqua, font=('Arial', 11, 'bold'), fg="blue").grid(row=2, column=1)

can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]

def chuyen():
    try:
        nam = int(nam_duong.get())
        ketqua.set(f"{can[nam % 10]} {chi[nam % 12]}")
    except:
        ketqua.set("Năm không hợp lệ!")

Button(root, text="Chuyển", command=chuyen, bg="yellow").grid(row=1, column=1, pady=10)

root.mainloop()
