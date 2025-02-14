def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = node = ListNode()  # Initialize a dummy node to simplify handling the head of the merged list

    while list1 and list2:  # Iterate until one of the lists is empty
        if list1.val < list2.val:
            node.next = list1  # Attach the smaller node to the merged list
            list1 = list1.next  # Move to the next node in list1
        else:
            node.next = list2  # Attach the smaller node to the merged list
            list2 = list2.next  # Move to the next node in list2
        node = node.next  # Move the node pointer to the newly added node

    node.next = list1 or list2  # Attach the remaining part of the non-empty list

    return dummy.next  # Return the merged list starting from the first real node


# Time Complexity: O(n + m)
# - We traverse through both lists once, where n is the length of list1 and m is the length of list2.

# Space Complexity: O(1)
# - We are using only a constant amount of extra space for the dummy node and pointers.
