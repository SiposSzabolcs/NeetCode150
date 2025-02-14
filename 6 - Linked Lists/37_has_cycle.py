def hasCycle(head):
    slow, fast = head, head
    # Check for edge case where the list is empty or has only one node
    if not head or not head.next:
        return False
    while fast and fast.next:
        slow = slow.next         # Move slow pointer by 1 step
        fast = fast.next.next    # Move fast pointer by 2 steps
        if slow == fast:  # If they meet, there is a cycle
            return True
    return False  # If fast pointer reaches the end, no cycle

# Time Complexity: O(n) where n is the number of nodes in the list.
# - In the worst case, both the slow and fast pointers traverse the list once, which takes linear time.
# Space Complexity: O(1)
# - Only two pointers are used (slow and fast), so the space complexity is constant.