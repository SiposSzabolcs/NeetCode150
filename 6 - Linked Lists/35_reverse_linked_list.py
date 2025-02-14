def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head  # Initialize pointers for previous and current nodes

    while curr:
        temp = curr.next  # Temporarily store the next node
        curr.next = prev  # Reverse the link
        prev = curr  # Move prev pointer to the current node
        curr = temp  # Move to the next node in the list

    return prev  # Return the new head of the reversed list


# Time Complexity: O(n)
# - We traverse through the entire list once, visiting each node once.

# Space Complexity: O(1)
# - We are only using a constant amount of extra space for the pointers `prev`, `curr`, and `temp`.
