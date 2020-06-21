import turtle
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