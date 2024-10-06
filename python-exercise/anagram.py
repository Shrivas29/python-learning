#method 1
# from collections import defaultdict

# def group_anagrams(words):
#     anagram_dict = defaultdict(list)

#     for word in words:
#         sorted_word ="".join(sorted(word))
#         anagram_dict[sorted_word].append(word) 

#     results = list(anagram_dict.values())
#     return results
 
# input_words = ["cat" , "ate" , "eat" , "tea"]
# output = group_anagrams(input_words)
# print(output)        

#method 2 
str = ["cat","ate","eat","tea"]
dic = {}
def finding_same():
    for x in str:
        print(x)
    w = "".join(sorted(x))
    print(w)
    
    if x in dic:
        dic[x].append(x)
    else:
        dic[w] = [x]
print(list(dic.values()))

finding_same()
