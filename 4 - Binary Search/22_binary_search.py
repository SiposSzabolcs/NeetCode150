def search(nums, target):
    # Initialize left and right pointers for binary search
    l = 0
    r = len(nums) - 1
    
    while l <= r:
        # Calculate middle index to avoid overflow
        m = l + ((r - l) // 2)
        
        # If middle element is greater than target, search left half
        if nums[m] > target:
            r = m - 1
        # If middle element is smaller than target, search right half
        elif nums[m] < target:
            l = m + 1
        # If target is found, return its index
        else:
            return m
    
    # If target is not found, return -1
    return -1

# Time Complexity: O(log n) since binary search repeatedly halves the search space.
# Space Complexity: O(1) since we use only a few extra variables.
