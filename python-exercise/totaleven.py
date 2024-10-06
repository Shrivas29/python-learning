# [1,2,3,4,5,6,7,8,9,10]
# nums = [1,2,3,4,5,6,7,8,9,10]
nums = [22,23,24,25,]
def even():
    sum = 0
    for i in nums:
        nums_1 = i % 2 == 0
        if nums_1 == True:
            sum = sum + i
            print(sum)
            # print(sum+= i)
    return sum
        
even()