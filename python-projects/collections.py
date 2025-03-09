#output = {"vowels":12,"consonants":17,"other":8}

def collections():
    collec = {"vowels":0,"consonants":0,"others":0}
    lis_vowels = ["a","e","i","o","u"]
    sentance = "i love python and it so easy to learn"

    for i in sentance.lower():
        if i.isalpha():
            
            if i in lis_vowels:
                collec["vowels"] += 1
                print(collec)
            else:
                collec["consonants"] += 1

        else:
            collec["others"] +=1 
collections()