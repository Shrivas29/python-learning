
## opening statements to ask the users 
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
def calculatore():
    should_acccumilate = True
    first_num = float(input("what is the first number"))
    while should_acccumilate:
        operrations_1 = input("what operations u wanna do is it '+','-','*','/'")
        second_num = float(input("what is the sencond number"))
        answer = operations[operrations_1](first_num,second_num)
        print(answer)

        countinue = input("type 'y' to countinue and 'n' to restart")
        if countinue == "y":
            first_num = answer
        else:
            should_acccumilate = False
            print("\n" * 20)

calculatore()
