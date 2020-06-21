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