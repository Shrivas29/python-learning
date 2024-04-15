#weight 0 to 25 (child)
#22 to 30 (women)
#greater 50 (old people)

#and , is

#function should have return and paprameter 

def calculate_weight():
    weight = int(input("what is you wieght??"))

    if weight >= 0 and weight <= 25:
       print("you  are  child")
    elif weight > 25 and weight <= 50:
       print("you are a women or men ")
    else:
        print("you are A OLD PERSON")

calculate_weight()               