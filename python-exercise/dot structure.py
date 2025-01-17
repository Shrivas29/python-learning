# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).



def remove_element(nums): #we are calling a function and naming at remove_element we are giving parameter as nums
    i = 0 #i as jar

    for num in nums: #we are looping through all the elements 
        if i < 2 or num > nums[1-2]:

            nums[i] = num

            i += 1

    return i
nums = [1,1,1,2,2,3]
k = remove_element(nums)
print(k)