import turtle

star = '*'
tstar = ' '

for x in range(1,6):
    for y in range(5-x):
        print(tstar, end = '')
    for z in range(2*x-1):
        print(star, end = '')
    print();
t = turtle.Turtle()

len = 100
for x in range(1,6):
    for y in range (4):
        t.forward(len)
        t.left(72)
    
    t.forward(len)
t.hideturtle()
