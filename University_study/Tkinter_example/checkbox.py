from tkinter import *
top = Tk()
top.title("체크박스")
def result():
    result = ""
    if int(chk1c.get()): 
        result += "체크박스1 "
    if int(chk2c.get()): 
        result += "체크박스2 "
    if int(chk3c.get()): 
        result += "체크박스3 "
    print(result)
    lb1['text'] = result
chk1c = IntVar()
chk2c = IntVar()
chk3c = IntVar()

fr = Frame(top)
chk1 = Checkbutton(top, text="체크박스1", variable=chk1c)
chk2 = Checkbutton(top, text="체크박스2", variable=chk2c)
chk3 = Checkbutton(top, text="체크박스3", variable=chk3c)
btn = Button(top, text="제출",command=result)
chk1.grid(row=0, column=1)
chk2.grid(row=0, column=2)
chk3.grid(row=0, column=3)
btn.grid(row=0, column=4)
fr.grid(row=2,column=0)
lb1 = Label(fr,text="")
lb1.grid()

top.mainloop()