from tkinter import *
top = Tk()
top.title("체크버튼")
top.geometry("600x300")
cnvs = Canvas(top,width=550, height=250)
cnvs.config(bg='white')
cnvs.pack()

def draw():
    cnvs.delete(ALL)
    if chk1_chked.get() ==1:
        cnvs.create_rectangle(40,40,500,200)
    if chk2_chked.get() ==1:
        cnvs.create_oval(40,40,500,200)
    if chk3_chked.get() ==1:
        cnvs.create_line(40,40,500,200)
frm = Frame(top)
frm.pack()
chk1_chked = IntVar()
chk2_chked = IntVar()
chk3_chked = IntVar()
chk1 = Checkbutton(frm,text="직사각형",variable=chk1_chked, command=draw)
chk2 = Checkbutton(frm,text="타 원",variable=chk2_chked, command=draw)
chk3 = Checkbutton(frm,text="직 선",variable=chk3_chked, command=draw)
chk1.pack(side=LEFT)
chk2.pack(side=LEFT)
chk3.pack(side=LEFT)
top.mainloop()