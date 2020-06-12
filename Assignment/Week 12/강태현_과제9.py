from tkinter import *

top = Tk()
top.title("라디오버튼과 체크버튼")
cnvs = Canvas(top, width =500, height = 200,bg='white')
cnvs.grid(row=0, column=0)

def draw():
    cnvs.delete(ALL)
    pick=int(group_a.get())
    checked = int(ch.get())
    if checked==1:
        if pick == 1:  
            cnvs.create_rectangle(30,30,470,170,fill="pink")
        elif pick == 2:
            cnvs.create_oval(30,30,470,170,fill="pink")
        elif pick == 3:
            cnvs.create_line(30,30,470,170,fill="pink")
    else:
        if pick == 1:  
            cnvs.create_rectangle(30,30,470,170)
        elif pick == 2:
            cnvs.create_oval(30,30,470,170)
        elif pick == 3:
            cnvs.create_line(30,30,470,170)
group_a = IntVar()
ch = IntVar()
fr = Frame(top)
fr.grid()
rb1 = Radiobutton(fr,text="직사각형", variable=group_a, value = 1,command=draw)
rb2 = Radiobutton(fr,text="타원", variable=group_a, value = 2,command=draw)
rb3 = Radiobutton(fr,text="직선", variable=group_a, value = 3,command=draw)
chk1 = Checkbutton(fr, text="색채우기", variable=ch)
rb1.grid(row=1, column=1)
rb2.grid(row=1, column=2)
rb3.grid(row=1, column=3)
chk1.grid(row=1, column=4)

top.mainloop()
