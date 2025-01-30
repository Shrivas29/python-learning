## we have to add two list which are non negative lists 
## lis = [1,2,3] lis2 = [4,5,6]
## output [9,7,5]
## explination = 654 + 321

lis_1 = [1,2,3]
lis_2 = [4,5,6]
for i in zip(lis_1,lis_2):
    summing_lists = sum(i)
    print(summing_lists)