class Car:

    # class varaibale
    TYPE = '4 wheeler'

    # magic method 1
    def _init_(self, make, model, color, year):
        # instance variable
        self.make = make
        self.model = model
        self.color = color
        self.year = year

    # magic method 2
    def _str_(self):
        return "this is a car class which holds make information"

    def drive(self):
        print("the " + self.model + " is currently driving")

    @staticmethod
    def stop(make):
        print("the method is a stop method and the make is " + make)

#object
car_1 = Car("honda", "civic", "grey", 2020)
car_2 = Car("kia", "sonate", "blue", 2024)

#printing the class variable
print(car_1.TYPE)

#printing the class variable
print(car_1)

# call function using the object
car_1.drive()
car_2.drive()

# calling a static method
Car("honda", "civic", "grey", 2020).stop("honda")