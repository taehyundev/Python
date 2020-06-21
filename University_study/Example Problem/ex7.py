from tkinter import * 
top = Tk()
def Excersize():
    print("총 소모 칼로리 ",(156*int(en1.get())))


Label(top, text="칼로리 계산").grid(row=0,column=0)
Label(top, text="운동시간 ").grid(row=1,column=0)
en1 = Entry(top)
btn1 = Button(top, text="계산",command=Excersize)
btn2 = Button(top, text="종료",command=lambda :top.quit())
en1.grid(row=1, column=1)
btn1.grid(row=2, column=0)
btn2.grid(row=2, column=1)

top.mainloop()