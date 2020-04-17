result = []
subject = []
subject.append(int(input("국어 점수는 : ")))
subject.append(int(input("수학 점수는 : ")))
subject.append(int(input("영어 점수는 : ")))
subject.append(int(input("과학 점수는 : ")))
subject.append(int(input("사회 점수는 : ")))
print("입력 자료 :", subject)

subject.sort()
subject.reverse()
result = subject
print("정렬 자료 :", result)

avg = (result[0] + result[1] + result[2] + result[3] + result[4])/ 5
print("평균 점수 :", avg)


import turtle
t = turtle.Turtle()
t.shape('turtle')

list_color = []


list_color.append('red')
list_color.append('green')
list_color.append('blue')

t.begin_fill()
t.fillcolor(list_color[0])
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(200)
t.end_fill()

t.begin_fill()
t.fillcolor(list_color[1])
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(200)
t.end_fill()

t.begin_fill()
t.fillcolor(list_color[2])
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.end_fill()
