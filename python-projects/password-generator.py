import random 


# Lowercase alphabets
lowercase_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# Symbols
symbols_1 = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']


print('welcome to password generatore app')

letter = int(input("how many letter u want in your password"))
number = int(input("how many number u want in your password"))
symbols = int(input("how many symbols u want in your password"))


#easy method 
password = ""

for i in range(1,letter +1):
    ran_l = random.choice(lowercase_alphabets)
    password += ran_l

for i in range(1,number + 1):
    ran_n = random.choice(numbers)
    password += ran_n
    print(password)

for i in range(1,symbols + 1):
    ran_s = random.choice(symbols_1)
    password += ran_s

print(password)