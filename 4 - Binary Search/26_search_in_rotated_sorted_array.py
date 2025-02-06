def search(nums, target):
    l, r = 0, len(nums) - 1  # Initialize pointers

    while l <= r:  # Standard binary search loop
        m = l + ((r - l) // 2)  # Midpoint calculation
        
        if nums[m] == target:  # Check if mid element is the target
            return m
        
        # Determine if the left half is sorted
        if nums[l] <= nums[m]:
            # Check if target is in the left sorted half
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:  # Otherwise, the right half must be sorted
            # Check if target is in the right sorted half
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    
    return -1  # Target not found

# Time Complexity: O(log n) (binary search in a rotated sorted array)
# Space Complexity: O(1) (only a few integer variables are used)

