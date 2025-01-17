# Input: nums = [3,2,3]
# Output: 3

nums = [3,2,3]

def majority(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num 

    count += (1 if num == candidate else -1)
    return candidate
print(majority(nums))