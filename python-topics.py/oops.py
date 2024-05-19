class Car:

    def __init__(self,make,model,color,year):

        self.make = make
        self.model = model
        self.color = color
        self.year = year

    def drive(self):
        print("the "+self.model+" is currently driving")

    def stop(self):
        print("the "+self.model+" is currnetly stopped")

    
car_1 = Car("honda","civic","grey",2020)
car_2 = Car("kia","sonate","blue",2024)

car_2.drive()
car_2.stop()
