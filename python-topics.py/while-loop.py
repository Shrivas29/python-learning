#while loop usually runs until the statement is true 
def count():
    i = 1
    while 1 > 6:
        print(i)
        i += 1
count()

#we can use break function 
def count_1():
    w = 2
    while 2 > 6:
        if w == 4:
            break 
        else:
            print(w)

count_1()