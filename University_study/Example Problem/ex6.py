from tkinter import *

top = Tk()
'''
Button(top, text="위쪽",width=10).pack(side=TOP)
Button(top, text="아래쪽",width=10).pack(side=BOTTOM)
Button(top, text="왼쪽",width=10).pack(side=LEFT)
Button(top, text="오른쪽",width=10).pack(side=RIGHT)
'''
day = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
for i in range(len(day)):
    Label(top, text=day[i],width=5).grid(row=0, column=i)

date_column = 2
date_row =1
for i in range(1,31):
    if (date_column) % 7 ==0:
        date_column = 0
        date_row = date_row+1
    Label(top, text=i,width=5).grid(row=date_row, column=date_column)
    date_column = date_column+1

top.mainloop()