from random import *
import turtle
#1 번문제

a = int(input("a 입력 : "))
b = int(input("b 입력 : "))

if a > b:
    print("a가 b보다 %d 만큼 더 크다" %(a-b))
elif a <b:
    print("b가 a보다 %d 만큼 더 크다" %(b-a))
else:
    print("같다")




#2 번문제
comList = ["가위", "바위","보"]
# 0 : 가위, 1 : 바위, 2 : 보

userSelect = input("가위, 바위, 보 : ")
comSelect  = randint(0,2)

if userSelect == comList[comSelect]:
    print("비겼습니다.")
else :
    if userSelect == "가위":
        if comList[comSelect] == "보":
            print("승")
        else:
            print("패")
    elif userSelect == "바위":
        if comList[comSelect] == "가위":
            print("승")
        else:
            print("패")
            
    elif userSelect == "보":
        if comList[comSelect] == "바위":
            print("승")
        else:
            print("패")


#3 번문제

t = turtle.Turtle()
t.shape('classic')
n1 = int(turtle.textinput('입력창', '변1: '))
n2 = int(turtle.textinput('입력창', '변2: '))
n3 = int(turtle.textinput('입력창', '변3: '))


if (n3*n3) == (n2*n2) + (n1 * n1):
    t.forward(n1*100)
    t.left(90)
    t.forward(n2*100)
    t.home()
else:
    t.write('직각삼각형이 아님.', font=("Arial",10))


