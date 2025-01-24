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
def calculate_score(cards):
    if sum(cards) ==  21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

        return sum(cards)


user_card = []
computer_card = []
game_over = False

for i in range(2):
    new_card = deal_card()
    user_card.append(new_card)
    computer_card.append(new_card)
user_score = calculate_score(user_card)
computer_score = calculate_score(computer_card)
print(f"your cards are{user_card} adn your socre is {user_score}")
print(f"computers cards are {computer_card} and the computer score is {computer_score}")


if user_score == 0 or computer_score == 0 or user_score > 21:
    game_over = True
else:
    extra_card = input("type 'y' to get 1 card and type 'n' if u dont want card")
    if extra_card == "y":
        user_card.append(new_card)
        
    else:
        game_over = True


