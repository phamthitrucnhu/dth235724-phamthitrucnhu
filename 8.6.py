from tkinter import *

root = Tk()
root.title("Style cho Button")
root.geometry("400x250")

styles = ['flat', 'raised', 'sunken', 'groove', 'ridge', 'solid']

Label(root, text="Các kiểu style của Button:", font=('Arial', 12, 'bold')).pack(pady=10)

for style in styles:
    Button(root, text=style, relief=style, width=15).pack(pady=5)

root.mainloop()
