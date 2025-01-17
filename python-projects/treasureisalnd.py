print("welcome to treasure island")
print("your mesion is to find the correct pathway by choosing either left or right")

a = input("left or right")
print(a)

if a == "left":
    b = input("swim or wait")
    print(b)
    if b == "wait":
        c = input("which door yellow or red or blue")
        print(c)
        if c == "yellow":
            print("you win")
        else:
            print("you are eleminated")
    else:
        print("attacked by a alligatore") 
else:
    print("fall into a hole")       


    