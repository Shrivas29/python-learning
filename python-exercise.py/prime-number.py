def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def calculate_prime():
    num1 = int(input("enter a starting range"))
    num2 = int(input("enter a end range"))
    # if not 1 <= num1 <= 10:
    #     print("please enter the number in the given range")
    #     import sys
    #     sys.exit()
    for i in range(num1,num2):
       if is_prime(i+1):
         
         print(f"{i+1} is a prime number ")
       else:
         print(f"{i+1}its not a prime number")
    
       
calculate_prime()
# # while True:
# #         num1 = int(input("Please enter a number between 40 and 100: "))


#         if 40 <= num <= 100:
#             if is_prime(num):
#                 print(f"{num} is a prime number.")
#             else:
#                 print(f"{num} is not a prime number.")
#         else:
#             print("Please enter a number within the specified range.")
   

#print(is_prime(2))    
#print(is_prime(23))

# range of numbers 1 to 10 
# loop a number, range of function 
# idenity prime no => is_prime 
    # if num <=1 dont coonsier 
    # check if number is divsible by 2 or 3 , use % modulo
    # 
# if it is a prime number,  print 
# jf it is not prime no we need to skip it 


# even number and odd numbner 
# first input 
# even numebr 
