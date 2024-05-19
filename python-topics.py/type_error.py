#type error
x = 10
y = "string" 
def value_type(x,y):
    try:
        k = x/y
    except ValueError as f:
        print("there is an problem",f)
value_type()