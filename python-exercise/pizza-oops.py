class Pizza:
    slices = 6

    def __init__(self,topping,company,prize,type):
        self.topping = topping
        self.company = company
        self.prize = prize 
        self.type = type

    def started(self):
        print(f"this {self.type} just started cooking")
    def finished(self):
        print(f"this {self.type} just started cooking")

    @staticmethod
    def middle(type):
        print("and the pizza name is" + type)
            
pizza1 = Pizza("cheese","dominos",7,"veg")
pizza2 = Pizza("beef","pizza hut",10,"non veg")

pizza1.started()
pizza2.started()
 
#calling a static method

Pizza.middle("non veg")

