def twoSum(numList, target):
    # Initialize two pointers
    l = 0
    r = 1
    
    while True:
        # Check if the current pair sums to the target
        if numList[l] + numList[r] == target:
            return [l, r]
        
        # If we haven't reached the end of the list with the right pointer
        if r < len(numList) - 1:
            r += 1
        else:
            # Exit if l pointer is at the last element of the list
            if l + 1 > len(numList) - 1:
                return None
            # If we've reached the end, move the left pointer and reset the right
            l += 1
            r = l + 1
        
'''
Time Complexity: O(n^2) in the worst case due to nested iterations over the list. 
Best case O(1) if solution found at first check.
Space Complexity: O(1) as we only use two variables regardless of input size.
'''