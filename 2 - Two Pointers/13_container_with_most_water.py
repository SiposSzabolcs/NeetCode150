def maxArea(heights):
    # Initialize two pointers at both ends of the array
    l = 0
    r = len(heights) - 1
    curr_max = 0  # Tracks the maximum water container size found

    while True:
        # If both pointers meet, return the maximum area found
        if l == r:
            return curr_max

        # Calculate the current area based on the smaller height
        curr = (r - l) * min(heights[l], heights[r])

        # Update max area if the current area is larger
        if curr > curr_max:
            curr_max = curr

        # Move the pointer with the shorter height inward to potentially find a larger area
        if heights[l] > heights[r]:
            r -= 1
        elif heights[l] < heights[r]:
            l += 1
        else:
            # If both heights are the same, arbitrarily move the right pointer
            r -= 1

# Space Complexity: O(1) - Uses only two pointers and a few variables.
# Time Complexity: O(n) - Each element is processed at most once as the two pointers move inward.
