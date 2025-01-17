# we have to create a game which should ask the interface of the user 
# they have to choose if it is rock or paper or scissors and check it with our computer answer 
# we need to import the random module 
# create 3 variable which is rock , paper and scissors 
# this is the syeps neesded for us finding the code outputs 
import random 
computer_ans = ["rock","paper","scissors"]

computer = random.choice(computer_ans) ## the random module is used for us to get the random selection of the list:computer_ans 
interface = input("rock or paper or scissors") ## we are asking for the interface answer
print(computer)
## rock

if interface == "rock" and computer == "paper":
    print("computer wins")

elif interface == "rock" and computer == "scissors":
    print("you win")

elif interface == "rock" and computer == "rock":
    print("its draw")

else:
    print("give valid input")


## paper 

if interface == "paper" and computer == "rock":
    print("you win")

elif interface == "paper" and computer == "scissors":
    print("computer wins")

elif interface == "paper" and computer == "paper":
    print("its draw")

else:
    print("enter a valid input")


## scissors

if interface == "scissors" and computer == "scissors":
    print("its a draw")

elif interface == "scissors" and computer == "rock":
    print("you lose")

elif interface == "scissors" and computer == "paper":
    print("you win")

else:
    print("enter a valid input")


## now we have a problem when we enter a particular answer the conditional statments should only work for those elements and not trigger other elements 
## we have to fix it 
