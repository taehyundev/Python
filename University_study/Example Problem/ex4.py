from tkinter import *
top = Tk()
def EnterHandler(event):
    if event.char == '\r':
        lb2['text'] = "결과:"+eval(en1.get())
lb1 = Label(top,text="파이썬 수식 입력: ")
en1 = Entry(top)
en1.bind('<Key>', EnterHandler)
lb2 = Label(top)
lb1.pack()
en1.pack(fill='x')
lb2.pack()
top.mainloop()
## <Return>은 엔터키