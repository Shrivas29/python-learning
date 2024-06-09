def is_subarray(arr1,arr2):

    n ,m = len(arr1) ,len(arr2)
    
    if m > n:
     return False #the fact that if an array has more numbers than the sub array then it cant be the subarray of the first array
    
    for i in range(n - m + 1): # we are ittirating throught the first array
       if arr1[i:i + m] == arr2:
          return True
       

       return False
    
#this case is subsiquance of first array 
# arr1 = [1,2,3,4,5]
# arr2 = [2,3,4]
# print(is_subarray,arr1,arr2) 

#this below case is not a subsiquance 
arr1 = [1,2,3,4,5]
arr2 = [2,4]
print(is_subarray,arr1,arr2)