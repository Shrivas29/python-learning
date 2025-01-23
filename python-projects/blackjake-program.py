## our blackjake game rules

#the deck is unlimited
#there are no jokers 
#the jake/queen/king all count as king
#the ace can count as one or eleven 
#the computer is the dealer

import random
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card 

user_card = []
computer_card = []

for i in range(2):
    new_card = deal_card()
    user_card.append(new_card)
    computer_card.append(new_card)

