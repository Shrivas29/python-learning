import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

knife = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇


images = [rock , paper , knife]

user_choice = int(input("what do you wanna choose? type0 for rock, type 1 for knife, type 2 for paper.\n"))
computer_choice = random.randint(0,2)
print(f"computer chose,{computer_choice}")
if user_choice >=3 or user_choice < 0:
  print("you have typed an invalid number")
else: 
  print(images[computer_choice])
  if user_choice == 0 and computer_choice == 2:
    print("you won")
  elif user_choice ==2 and computer_choice ==0:
    print("you lost")
  elif user_choice == computer_choice:
    print("its a draw")
  elif user_choice > computer_choice:
    print("you won")
  elif computer_choice > user_choice:
    print("you lost")
  else:
    print("you typed an invalid number, you lose")
