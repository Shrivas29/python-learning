#args allows you to pass multiple non keyword arguments 
#example 1
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,3))

#example 2
def name(*args):
    for arg in args:
        print(arg,end = " ")

name("shrivas","venkatasami","murali")
#kwargs
#allows you to pass many key wrod arguments

def location(**kwargs):
    for key in kwargs.keys:
        print(key)
location(appartement = "SGV",BLOCK = "c2")

#palindrome
def vari():
    n = input("enter a string ")
    if n == n[::-1]:
        print("it is a palindrom")
    else:
        print("its not a plindrome")
vari()




    