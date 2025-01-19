## bid selection game 
## creating a function to find which bidder is higher 

def find_high(bid_dict):
    winner = ""
    highest_bid = 0 
    for bidder in bid_dict:
        bid_amount = bid_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"the winner is {winner} and the bid amount is {bid_amount}")



        


countine = True
dic = {}
while countine:
    name = input("what is your name: ") ## asking names 
    bid = float(input("what is your bid"))  ## asking bid
    dic[name] = bid 
    should_countinue = input("are there more users 'yes' or 'no' ").lower()
    if should_countinue == "no":
        countine = False
        find_high(dic)

    elif should_countinue == "yes":
        print("/n"*20)


