class Shape:
    def __init__(self,lenght,height,breadth):
        self.lenght = lenght
        self.height = height 
        self.breadth = breadth 

class Cube(Shape):
     def __init__(self,lenght):
        super().__init__(lenght)
     def area(self):
      return self.lenght * self.lenght * self.lenght
     
class Square(Shape):
    def __init__(self,lenght,height):
        super().__init__(lenght,height)
    def area1(self):
        return self.lenght * self.height
class Rectangle(Shape):
    def __init__(self,lenght,height,breadth):
        super().__init__(lenght,height,breadth)
    def area2(self):
        return self.lenght * self.height * self.breadth 
    

height = int(input("what is the height "))
lenght = int(input("what is the weight"))
breadth = int(input("what is the breadth"))

rectangle = Rectangle(lenght,height,breadth)
square = Square(lenght,height)
cube = Cube(lenght)

print(square.area1())