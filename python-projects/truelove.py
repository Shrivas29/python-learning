def callculate_love(name1,name2):
    combine_names = name1.lower() + name2.lower()

    true = sum(combine_names.count(letter) for letter  in "true")

    love = sum(combine_names.count(letter) for letter in "love") 

    score = int(f"{true}{love}")

    print(score)

callculate_love("nithilan","aashrutha")

