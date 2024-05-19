#Python Exception Handling
#zero devision
a = input(int("price of a shoot is ?"))
b = 0
def price(a,b):
    try:
        x =  a/b
        print(x)
    except Exception as e:
        print("this is the error",e)
    finally:
        print("we are all set")
price()

#type error
x = 10
y = "string" 
def value_type(x,y):
    try:
        k = x/y
    except ValueError as f:
        print("there is an problem",f)
value_type()

#syntax error
def anto():
    a = 500
    if a < 100
    print("a is greater than nnumbers till 499")
anto()

#key error
def dict_1():
    A = {"apple":"red","banana":"yellow"}
    try:
        k = A.get["orange"]
        print(k)
    except KeyError as e:
        print("key not found",e)
dict_1()

#file error
try:
    k = open("demofile.txt", "r")
    print(k)
except FileNotFoundError:
    print("the given file was not found")