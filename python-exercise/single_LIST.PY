l1 = [1,2,3]
l2 = [1,2,3]

def add():

    empty = []
    for i,j in zip(l1,l2):
        empty = i + j 
        print(empty)
add()
