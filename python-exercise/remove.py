# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# # It does not matter what you leave beyond the returned k (hence they are underscores).

nums = [3,2,2,3]
val = 3

k = 0 
def remove(k):
    for i in range(len(nums)):
        if nums[i] != val:          # when the number is not equall to val then the number is added to k
            nums[k] = nums[i]       # here the number 2 has been added 
            k += 1

        return k
remove(k)


