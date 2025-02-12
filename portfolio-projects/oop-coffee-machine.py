MENU = {"espresso":{"ingreidients": {"water": 50,"coffee": 18},"cost":2},##### this is the menu we will be working with 
    "latte":{"ingreidients": {"water": 200,"milk":150,"coffee": 24},"cost":5},
    "cappachino":{"ingreidients": {"water": 250,"milk":100,"coffee": 24},"cost":6}}
resource = {"water":300,"milk":200,"coffee":100,"money":0}#### this is the resources the coffee machine will be having 
class Coffee_maker:
    def __init__(self):
        resource = {"water":300,"milk":200,"coffee":100,"money":0}
        

is_on = True
while is_on is True:    
    choice = int(input("what would you like (espresso/latte/cappachino)"))
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(resource["water"])
        print(resource["milk"])
        print(resource["coffee"])
        print(resource["money"])




