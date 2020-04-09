
#과제2
import turtle
t = turtle.Turtle()
t.shape('classic')

s = turtle.textinput('입력창', '그림 색: ')
t.color(s)

t.penup()
t.goto(31,73)
t.write('Stop', font=("Arial",15,"bold"))
t.home()
t.pendown()
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)

#과제1
name1 = input('이름 첫째자는 : ')
name2 = input('이름 둘째자는 : ')
name3 = input('이름 셋째자는 : ')
print('*' * len(name1 + name2 + name3))
print(chr(ord(name2[0])+32) + chr(ord(name3[0])+32) + chr(ord(name1[0])+32) + name1[1:])

