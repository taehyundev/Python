from tkinter import *
top = Tk()
top.title("라디오 버튼")
def choiceMenu():
    rtn = "선택한 메뉴의 금액 : "+ str(ch.get())
    lb1['text'] = rtn

ch = IntVar()

rb1 = Radiobutton(top, text="아메리카노", value=5000, variable= ch, command=choiceMenu)
rb2 = Radiobutton(top, text="카푸치노", value=4500, variable= ch, command=choiceMenu)
rb3 = Radiobutton(top, text="까페라떼", value=4000, variable= ch, command=choiceMenu)
lb1 = Label(top, text="")
rb1.pack()
rb2.pack()
rb3.pack()
lb1.pack()
top.mainloop()