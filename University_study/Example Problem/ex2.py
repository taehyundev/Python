class Rectangle:
    def __init__(self,width=1, height=1):
        self.__width = width
        self.__height = height
    def getArea(self):
        return self.__width* self.__height
    def getPerimeter(self):
        return (self.__width*2)+(self.__height*2)

r = Rectangle(1,2)
print(r.getArea())
print(r.getPerimeter())