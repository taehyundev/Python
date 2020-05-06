import turtle
#문제1
t = turtle.Turtle()
t.shape('turtle')

def cCircle(r):
    t.penup()
    t.goto(0,-r)
    t.pendown()
    t.circle(r)
    t.penup()
    t.goto(0,0)
    t.pendown()
    return r
    
print(cCircle(100))
print(cCircle(70))
print(cCircle(40))

#문제 2

def toBinary(data):
    result = ""
    while(1):
        if data == 0 or data == 1:
            result = str(data) + result
            return result
        result = str(int((data % 2))) + result
        data = int(data / 2)

def toDecimal(data):
    mem = 1
    result = 0
    for i in range(0, len(data)):
        if int(data[len(data)-1-i]) == 1:
            result = result + mem 
        mem = mem * 2
    return result

print(toBinary(int(input("10진수: "))))
print(toDecimal(input("2진수: ")))

