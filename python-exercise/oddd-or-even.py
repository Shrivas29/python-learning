def vari():
    starting_range  = int(input("enter a starting range"))
    ending_range = int(input("enter an ending range"))
vari()

def find_even(starting_range,ending_range):
    for x in range(starting_range,ending_range):
        if x % 2 == 0:
            print("its an even number")
        else:
            print("its an odd number")
    return starting_range , ending_range
find_even(starting_range,ending_range) # type: ignore
