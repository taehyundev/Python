from tkinter import *
top = Tk()
def ADD():
    global rtn 
    rtn=int(en1.get()) + int(en2.get())
    lb2['text']= "결과는 "+str(rtn)

rtn=int()
en1 = Entry(top,width=3)
lb1 = Label(top, text="+")
en2 = Entry(top,width=3)
btn1 = Button(top, text="결과", command = ADD)
lb2 = Label(top,text="")

en1.grid(row=0, column=0)
lb1.grid(row=0, column=1)
en2.grid(row=0, column=2)
btn1.grid(row=1, column=0)
lb2.grid(row=2, column=0)
top.mainloop()