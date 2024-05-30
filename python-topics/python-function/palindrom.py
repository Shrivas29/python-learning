#palindrome
def vari():
    n = input("enter a string ")
#    if n == n[::-1]:
#        print("it is a palindrom")
#    else:
#        print("its not a plindrome")
#vari()


#using palindrome in args
n = input("enter a string?")
def check_palin(*args):
    m = args[0]
    if n == n[::-1]:
      print("it is a palindrom")
    else:
      print("its not a plindrome")

check_palin(n)





    