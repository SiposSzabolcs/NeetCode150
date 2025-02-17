# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)  # Dummy node to handle edge cases
    left = dummy
    right = head
    # Move right pointer n steps ahead
    while n > 0:
        right = right.next
        n -= 1
    # Move both pointers until right reaches the end
    while right:
        left = left.next
        right = right.next
    # Remove the nth node
    left.next = left.next.next
    return dummy.next  # Return the head of the modified list

# Time Complexity: O(n)
# - Moving the right pointer n steps takes O(n).
# - Moving both pointers until the right reaches the end takes O(n - n) ≈ O(n).
# - Modifying the linked list takes O(1).
# - Overall, O(n) + O(n) + O(1) = O(n).

# Space Complexity: O(1)
# - Only a few pointers are used, so the extra space required is constant.
