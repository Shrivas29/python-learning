#we have to create a hangman game with all the concepts which were learnt previously by us 

## we will be using concepts like modules,loops,list,string functions 

import random 
words = ["apple","camel","between","banana"]
words_random = random.choice(words)


# creating a placeholder 

placeholder = "_"
word_ran = len(words_random)

for position in range(word_ran):
    placeholder += "_"
    print(placeholder)

# we are creating a variable to store the empty string value 
correct = []
game_over = False
while not game_over:
    get_letter = input("enter a letter")
    display = ""
    
    for letter in words_random:
        if letter == get_letter:
            display += letter
            correct.append(get_letter)
        elif letter in correct:
            display += letter

        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("you win")