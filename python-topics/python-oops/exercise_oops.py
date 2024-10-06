class Car:
    def __init__(self,make,color,year):
        self.make = make
        self.color = color
        self.year = year

    def drive(self):
        print(f"this {self.make} is moving")

    def stop(self):
        print(f"this {self.make} is moving")

car_1 = Car("honda","black","1988")
car_2 = Car("audi","grey","2020")

car_1.drive()
car_2.stop()

        