#palindrome in kwargs 
n = input("enter a string?")
def check_palin(**kwargs):
    name = n 
    n = kwargs.get[name]
    if n == n[::-1]:
      print("it is a palindrom")
    else:
      print("its not a plindrome")

check_palin(n)


