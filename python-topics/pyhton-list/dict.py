#dict is a data type which contains keys and its value
goat = {"ronaldo":"FS","messi":"LW","neymar":"RW"}
print(goat)
#or if you want a specific value you print 
print(goat["ronaldo"])
#you can find the lenght of a particular dict
print(len(goat))

# u can access a particular dict by using 

goat.get["ronaldo"]

#you can use .key to get all the keys in a particular dict
goat.keys()

goat["ramos"] ="CB"

print(goat['ramos'])

# you can get value by using 
goat.values()

goat["messi"] ="CM"
print(goat["messi"])

#to find what keys and values are there in dict we use items 

print(goat.items())

#you can a change or update a keys value by

goat.update({"messi":"RB"})

#you can use the same update function to add a key and value to a existing dict



