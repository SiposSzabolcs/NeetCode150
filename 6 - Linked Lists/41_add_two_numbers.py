def addTwoNumbers(l1, l2):
    dummy = ListNode(0)  # Dummy node to simplify list creation
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0  # Get value from l1, or 0 if None
        val2 = l2.val if l2 else 0  # Get value from l2, or 0 if None
        
        total = val1 + val2 + carry
        carry = total // 10  # Carry for next iteration
        current.next = ListNode(total % 10)  # Store the last digit
        
        # Move forward in lists
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next  # Return the head of the new list


# Time Complexity: O(max(m, n))
# - We traverse both linked lists once, where m and n are their respective lengths.
# - The loop runs until both lists are exhausted, making it O(max(m, n)).

# Space Complexity: O(max(m, n))
# - We create a new linked list to store the sum, which has at most max(m, n) + 1 nodes (if there is a carry).
# - This results in O(max(m, n)) extra space for the new list.
