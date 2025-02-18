def findDuplicate(nums):
    for num in nums:
        idx = abs(num) - 1  # Get the index corresponding to the absolute value of num
        
        if nums[idx] < 0:  # If we’ve already visited this index (marked negative), return num
            return abs(num)
        
        nums[idx] *= -1  # Mark this index as visited by negating its value

    return -1  # Should never reach here (problem guarantees at least one duplicate)


# Time Complexity: O(n)
# - We iterate through the list once, modifying values in-place.
# - Each lookup and modification takes O(1), making the overall complexity O(n).

# Space Complexity: O(1)
# - We modify the input list in place, using no extra space apart from a few variables.
# - No additional data structures are used, so the space complexity remains O(1).