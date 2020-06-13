from tkinter import *
top = Tk()
userInfo = {"id":"taehyundev", "pw":"1234"}
#인증
def auth():
    if str(userInfo['id']) == str(en.get()) and str(userInfo['pw']) ==str(en1.get()):
        result['text'] = "인증이 완료되었습니다."
    else:
        result['text'] = "아이디 또는 비밀번호가 잘못되었습니다."

lb = Label(top,text="username ")
en = Entry(top)
lb1 = Label(top,text="password ")
en1 = Entry(top,show='*')
btn = Button(top,text="인증", command=auth)
result = Label(top)

#배치
lb.grid(row=0, column=0)
en.grid(row=0, column=1)
btn.grid(row=0, column=2, rowspan=2)
lb1.grid(row=1, column=0)
en1.grid(row=1, column=1)
result.grid(row=2, column=1)
top.mainloop()
