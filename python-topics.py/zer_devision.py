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