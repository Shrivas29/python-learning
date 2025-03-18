#sentance = "i love python and it is so easy to learn" sample output = {1;1,4:2,5:1,3:1,2:3,6:1}

def word_count():
    dict_1 = {}
    sentance = "i love python and it is so easy to learn"
    splite_1 = sentance.split()
    for i in splite_1:
        word_lenght = len(i)
        if word_lenght in dict_1:
            dict_1[word_lenght] += 1
        else:
            dict_1[word_lenght] = 1
            
    print(dict_1)
        

        
word_count()


        
        
        