# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reorderList(head):
    # Step 1: Find the middle of the linked list using slow and fast pointers
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the linked list
    second = slow.next
    prev = slow.next = None  # Cut the list into two halves
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp

    # Step 3: Merge the two halves
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2

# Time Complexity: O(n)
# - Finding the middle takes O(n/2) ≈ O(n).
# - Reversing the second half takes O(n/2) ≈ O(n).
# - Merging the two halves takes O(n).
# - Overall, O(n) + O(n) + O(n) = O(n).

# Space Complexity: O(1)
# - We modify the list in-place using only a few pointers, so the extra space used is constant.
