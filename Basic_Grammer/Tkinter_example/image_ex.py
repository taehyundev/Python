from tkinter import *
top =Tk()

top.title("이미지 넣기")
logo = PhotoImage(file="logo.png")
a =Label(top, image=logo).pack()
top.mainloop()