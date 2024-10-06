# ## input int problem 

# ## we need to create a code which is able to add the number given by the user base 

# ## solution 


# Prompt the user for the number of pairs
# Prompt the user for the number of inputs

try:
    
    num_inputs = int(input("Enter the number of numbers to input: "))

    numbers = []
    for i in range(num_inputs):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)


    result = sum(numbers)

    print(f"The sum of the entered numbers is: {result}")

except ValueError:
    print("Invalid input. Please enter numeric values.")

except TypeError:
    print("the given data type is not correct.please enter the correct data type")


