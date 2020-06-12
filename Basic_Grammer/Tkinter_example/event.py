from tkinter import *

top = Tk()

def key(event):
    print(event)

def mouse(event):
    print("<마우스>")
def motion(event):
    print(event)
frm = Frame(top, width=100, height=100)
frm.pack()

frm.focus_set()
frm.bind("<Key>", key)

frm.bind("<Button-1>", mouse)
frm.bind('<Motion>',motion)
top.mainloop()