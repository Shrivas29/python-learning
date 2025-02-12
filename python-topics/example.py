# exrtact 2 list slices out of a given list of numbers display and print the sum of elements of first list slice whichcontains every other elemt of the list
# between 5 to 15 program should also display the average of the elemnt in the second list slice that contains every 4rth element of the list 
# the given list contains number from 1 to 20 

# create 
#list
#two slices variable 
#have value = 0 and avg = 0
#loop into the slices to add into value 
#get the avg by divinding value/ken(slice2)


## steps 

# -- lis 
# -- sliceing the list and storing it to slice1
# -- sliceing the list into every fourth and stoing into a variable called slices2
# -- value = 0 and avg = 0
# -- we are loooping into slice 1 and adding it to the value 
# -- we are looping into slices2 and adding it to value 
# -- avg = value{sum of the slices}/len(slices2)


lis = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] # which contains all the number from 1 to 20 #1
slice1 = lis[5:15:2]#2
slices2 = lis[::4]
print(slice1)
value = 0
avg = 0 
for i in slice1: ## first slice
    value +=i
    print(i)

print(value)

for i in slices2: ## second slice 
    value +=i
    print(i)

print(value)
avg = value/len(slices2)
print(avg)