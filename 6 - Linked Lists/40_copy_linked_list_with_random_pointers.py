def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    if not head:
        return None
    
    # Step 1: Create new nodes and insert them next to the original nodes
    curr = head
    while curr:
        new_node = Node(curr.val, curr.next, None)
        curr.next = new_node
        curr = new_node.next
    
    # Step 2: Assign random pointers for the new nodes
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next
    
    # Step 3: Separate the two lists
    old_list = head
    new_list = head.next
    new_head = new_list
    while old_list:
        old_list.next = old_list.next.next if old_list.next else None
        new_list.next = new_list.next.next if new_list.next else None
        old_list = old_list.next
        new_list = new_list.next
    
    return new_head

# Time Complexity: O(n)
# - Step 1: Creating new nodes and inserting them takes O(n).
# - Step 2: Assigning random pointers takes O(n).
# - Step 3: Separating the two lists takes O(n).
# - Overall complexity: O(n) + O(n) + O(n) = O(n).

# Space Complexity: O(1)
# - No extra data structures are used; we modify the linked list in place.
# - The only extra space used is for the new nodes, which is part of the output.