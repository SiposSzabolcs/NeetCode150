def trap(height):
    # If the list is empty, no water can be trapped
    if not height:
        return 0

    # Initialize two pointers and their respective max heights
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0

    while left < right:
        # Move the pointer with the smaller max height inward
        if left_max < right_max:
            left += 1
            # Update the maximum height on the left side
            left_max = max(left_max, height[left])
            # Calculate trapped water at the current position
            water += max(0, left_max - height[left])
        else:
            right -= 1
            # Update the maximum height on the right side
            right_max = max(right_max, height[right])
            # Calculate trapped water at the current position
            water += max(0, right_max - height[right])

    return water

# Space Complexity: O(1) - Uses only a few variables, no additional data structures.
# Time Complexity: O(n) - Each element is processed once as the two pointers move inward.
