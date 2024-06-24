#method1(in) 
# def findhaystack(haystack,needle):
#     return needle in haystack

# #example usage 


# needle = "lol" # = download this example will give false since there is no doenload in hello world 
# haystack = "hello world" 
# print(findhaystack(haystack,needle)) #calling to check if the given example is true 

#method2(find)

def findneedle(haystack,needle):
    return haystack.find(needle)

#example usage 

needle = "world"
haystack = "hello world"
print(findneedle(haystack,needle))

