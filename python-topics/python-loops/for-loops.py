#for loops are used to iterate over a string, range, list and dict
#range
def count():
    for x in range(2, 10):
        print(x)
count()

#list
def count_1():
     fruits = ["apple","banana","mango"]
     for x in fruits:
       if x == "banana":
          break 
       print(x)
count_1()

#string
def count_2():
    for x in "banana":
        print(x)

count_2()
