##this is an challenge for you to run a code which appends both the list toghther in a new list 

## list1 = [1,2,3]   list2 = [4,5,6]
# list3 = [1,2,3,4,5,6]

list1 = [1,2,3]
list2 = [4,5,6]
list3 = []

for i in zip(list1,list2):
    list3.append(i)


print(list3)