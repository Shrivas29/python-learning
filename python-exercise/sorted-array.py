# sorted array problem

## we have to create a code which should be able to give us the index of word in the list called nums


## sloution method 1 (chatgpt)




# def search_insert(nums, target):
#     left, right = 0, len(nums) - 1
    
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
    
#     return left

# # Example usage:
# nums = [1, 3, 5, 6]
# target = 5
# print(search_insert(nums, target))  

## method 2(reference)


import bisect

def search_insert(nums, target):
    index = bisect.bisect_left(nums, target)
    return index

# Example usage:
nums = [1, 3, 5, 6]
target = 7
print(search_insert(nums, target))