from tkinter import *
top = Tk()

def change1():
    F = int(en1.get())
    C = (F - 32) / 1.8
    en2.insert(0, C)

def change2():
    C = int(en2.get())
    F = C * 1.8 + 32
    en1.insert(0, F)

lb1 = Label(top, text="화씨")
en1 = Entry(top)
lb2 = Label(top, text="섭씨")
en2 = Entry(top)
btn1 = Button(top, text="화씨->섭씨",command=change1)
btn2 = Button(top, text="섭씨->화씨",command=change2)
lb1.grid(row=0, column=0)
en1.grid(row=0, column=1)
lb2.grid(row=1, column=0)
en2.grid(row=1, column=1)
btn1.grid(row=2, column=0)
btn2.grid(row=2, column=1)
top.mainloop()