class Car:
    made = "carbon fiber"

    def __init__(self,model,company,color):

        self.model = model
        self.company = company 
        self.color = color
    def drive(self):
        print(f"this {self.model} is currntly is driving")

    def stop(self):
        print(f"thie {self.model} is currntly on stop")

class honda(Car):

    def __init__(self):
        print("this car is for midddle class")
    
    def drive(self):
        print(f"this {self.model} is on motion ")

    def stop(self):
        print(f"this {self.model} is not moving ")

class porche(Car):

    def __init__(self):
        print("this car is for the rich")

    def drive(self):
        print(f"this {self.model} is currently on motion")

    def stop(self):
        print(f"this {self.model} is on stop")
## multiple inhertance 

class hundai(porche,honda):

    def __init__(self):
        print("this car is for poor or low middel class ")
    
    def drive(self):
        print(f"this {self.model} is currently on motion")

    def stop(self):
        print(f"this {self.model} is on currently on stop")


car_1 = honda()
car_1.drive()
car_1.stop()

car_2 = porche()
car_2.drive()
car_2.stop()

car_3 = hundai()
car_3.drive()
car_3.stop()

