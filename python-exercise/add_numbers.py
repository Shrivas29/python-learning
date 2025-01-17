l1 = [2,3,4]
l2 = [4,5,6]

def addTwoNumbers(l1, l2):
    dummy = [0, None]  # Dummy node to simplify result handling
    current = dummy  # Pointer to construct the new list
    carry = 0  # Carry for digits sum

    while l1 or l2 or carry:
        # Get the values from the current nodes, or 0 if the list has ended
        val1 = l1[0] if l1 else 0
        val2 = l2[0] if l2 else 0

        # Compute the sum of current digits and carry
        total = val1 + val2 + carry
        carry = total // 10  # Update carry for the next position
        current[1] = [total % 10, None]  # Create a new node with the current digit

        # Move to the next positions in each "linked list"
        current = current[1]
        l1 = l1[1] if l1 else None
        l2 = l2[1] if l2 else None

    return dummy[1]  # Return the node after dummy as the result list
addTwoNumbers(l1,l2)