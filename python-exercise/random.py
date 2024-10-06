import random 

word = [1,2,3,4,5,6,7,8,9]

dog = random.choice(word)
user = input("eneter a number ")

if user in dog:
    print("you are right")
else:
    print("you are wrong")