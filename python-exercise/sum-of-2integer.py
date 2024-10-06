#method 1
# #example nums = [2,7,8,7]
# #example dict= {2:1,7:2,8:3,}
# #target = 14 
# class solution(object):
#     def twosum(self,nums,target):
#         d = {}

#         for i in range(0,len(nums)):
#             d[nums[i]] = i

#         for i in range(0,len(nums)):
#             x = target - nums[i]
#             if x in d and i != d[x]:
#                 return[i,d[x]]
            
#         return None
    
# # if we are able to run this code then the answer should be = 2:4

#method 2(using functions)

nums = [2,7,8,7]
target= 14

sum(nums, target)

def sums(num,target):

    d ={}
    
    for i in range(0,len(num)):
        d[num[i]] = i

    for i in range (0,len(num)):
        x = target - num[i]
        if x in d and i !=d[x]:
            return[i,d[x]]

    return None
