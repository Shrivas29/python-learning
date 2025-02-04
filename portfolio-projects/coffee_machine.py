# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.



# 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.


# 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5


# 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.


# 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52


# 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.


# 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:





#/\
#||
#||
#project discription_


amount = 0 

MENU = {"espresso":{"ingreidients": {"water": 50,"coffee": 18},"cost":2},##### this is the menu we will be working with 
    "latte":{"ingreidients": {"water": 200,"milk":150,"coffee": 24},"cost":5},
    "cappachino":{"ingreidients": {"water": 250,"milk":100,"coffee": 24},"cost":6}}

resource = {"water":300,"milk":200,"coffee":100,"money":0}#### this is the resources the coffee machine will be having 
def resource_suffi(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resource[item]:
            print(f"sorry resource is not sufficent enough{item}")
            is_enough = False
    return is_enough 

def procces_coins(total):
    print("please enter coins")
    total += int(input("how many quarters")) * 0.25
    total += int(input("how many dimes")) * 0.1
    total += int(input("how many nickel")) * 0.05
    total += int(input("how many pennies")) * 0.01
    return total

def transaction_succesful(money_recieved,drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost,2)
        print("here is the change")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry thats not enough money")
        print("the money will be refunded")
        return False

def make_coffee(drink_name,order_ingredeint):
    for item in order_ingredeint:
        resource[item] -= order_ingredeint[item]
    print(f"here is your{drink_name}")


is_on = True
while is_on:
    choice = input("what would you like(espresso/latte/cappachino)")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(resource["water"])
        print(resource["milk"])
        print(resource["water"])
        print(resource["money"])
    else:
        drink = MENU[choice]
        if resource_suffi(drink["ingreidients"]):
            payment = procces_coins(amount)
            if transaction_succesful(payment,drink["cost"]):
                make_coffee(choice,drink["ingreidients"])

       