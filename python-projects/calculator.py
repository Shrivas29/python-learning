
## opening statements to ask the users 
first_num = int(input("what is the first number"))
second_num = int(input("what is the sencond number"))
operrations_1 = input("what operations u wanna do is it '+','-','*','/'")


## create add,subract,multiply and divide function

## add
def add(n1,n2):
    return n1 + n2


## sub
def sub(n1,n2):
    return n1 - n2


##multiply
def multiply(n1,n2):
    return n1 * n2 


## divide 
def divide(n1,n2):
    return n1 / n2


## now create a dictionary which caontains all these function where the keys are "+","-","*","/"

operations = {"+":add,"-":sub,"*":multiply,"/":divide}


## use any function to calculate using the dictionary for example try calculating 4 into 4 

print(operations["*"](1,4))
