#we have to create a hangman game with all the concepts which were learnt previously by us 

## we will be using concepts like modules,loops,list,string functions 

import random

words = ["car","apple","orange","water","millon"]

word_random = random.choice(words)
print(word_random)
get_word = input("enter a letter ?")
print(get_word)

if get_word in word_random:
    print("you are one step closer")
else:
    print("you are wrong")

def blanks():
    dash =  ""
    for i in word_random:
        dash += "_"
        print(dash)
blanks()

def put():
    placements = ""
    for get_word in word_random:
        placements += get_word 
        print(placements)
put()

