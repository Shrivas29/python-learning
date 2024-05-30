def vari():
    bill = int(input("what is the total amount of the bill?"))
    people = int(input("how much people are spliting the bill"))
    tip = int(input("how much do you want to tip?"))
    return {"bill" : bill, "people": people,"tip":tip}

output = vari()
print(output)

def calculation(bill, people):

    a = bill / people
    print(a)
    b = a * tip
    print(b)
    return bill / people
output = vari()
print(output)
d = calculation(output['bill'],output['people'])
print(d)

    
