## we have two modes hard and easy 
## we can create two different function fro hard and easy modes
## we need the system to give clues based on the inputs given by the user
from random import randint
EASY = 10
HARD = 5
def check(check_num,actual_ans,turns):
    if check_num > actual_ans:
        print("too high")
        turns -=1 
        return turns
    elif check_num < actual_ans:
        print("too low")
        turns -=1 
        return turns
    else:
        print(f"you are correct{actual_ans}")

def set_defi():
    choice = input("choose dificulty 'easy' or 'hard'")
    if choice == "easy":
        return EASY

    else:
        return  HARD

def game():
    print("welcome to number guessing game")
    print("you have to guess a number between 1 to 100")
    turns = set_defi()
    print(f"you have {turns}")
    answer = randint(1,100)
    guess = 0 
    while guess != answer:
        guess = int(input("enter a number"))
        check(guess,answer,turns)
game( )
