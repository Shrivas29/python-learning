# prefix sorted array

## Write a function to find the longest common prefix string amongst an array of strings.

## solution 

def find_commonprefix(str):
    str = ["flow","flight","float"]
    res = ""

    for i in range(len(str[0])):
        for s in str:
            if i == len(s) or s[i] != str[0][i]:
                return res
        res += str[0][i]
    return res
print(find_commonprefix(str))
            