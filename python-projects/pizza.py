print("welcome to pizza deleveries")

size = input("what size you wanna order s, m or l").lower
peproni = input("do you want peporni Y or N").lower
extra_chess = input('do you want extra xhess Y or N').lower
print(size)
print(peproni)
print(extra_chess)
bill = 0
if size == "s":
    bill += 15
    if peproni == "Y":
        bill+=3
        if extra_chess == "Y":
            bill+=3



elif size == "m":
    bill += 20
    if peproni == "Y":
        bill+=3
        if extra_chess == "Y":
            bill+=3


else:
    bill += 30 
    if peproni == "Y":
        bill+=3
        if extra_chess == "Y":
            bill+=3
print(bill)



