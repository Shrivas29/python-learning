class Rectangle:

    def __init__(self,lenght,weight):
     
     self.weight = weight
     self.lenght = lenght   

class Square(Rectangle):
   def __init__(self,lenght,weight):
      super().__init__(lenght,weight)
   def area(self):
    return self.lenght*self.weight

class Cube(Rectangle):
   def __init__(self, lenght, weight,height):
      super().__init__(lenght, weight)
      self.height = height
   def volume(self):
      return self.lenght*self.weight*self.height 
   
square = Square(3,3)
cube = Cube(3,3,3)

print(square.area())
print(cube.volume())
