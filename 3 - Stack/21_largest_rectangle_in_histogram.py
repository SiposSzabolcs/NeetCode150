def largestRectangleArea(heights):
    n = len(heights)
    
    # Stack to find the leftmost smaller element for each bar
    stack = []
    leftMost = [-1] * n  # Stores indices of the nearest smaller element to the left
    for i in range(n):
        # Maintain a monotonic increasing stack
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            leftMost[i] = stack[-1]  # Store index of the leftmost smaller element
        stack.append(i)  # Push the current index onto the stack
    
    # Stack to find the rightmost smaller element for each bar
    stack = []
    rightMost = [n] * n  # Stores indices of the nearest smaller element to the right
    for i in range(n - 1, -1, -1):
        # Maintain a monotonic increasing stack
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            rightMost[i] = stack[-1]  # Store index of the rightmost smaller element
        stack.append(i)  # Push the current index onto the stack
    
    # Calculate the maximum area for each bar
    maxArea = 0
    for i in range(n):
        leftMost[i] += 1  # Convert to the actual boundary index
        rightMost[i] -= 1  # Convert to the actual boundary index
        width = rightMost[i] - leftMost[i] + 1  # Width of the rectangle
        maxArea = max(maxArea, heights[i] * width)  # Update max area
    
    return maxArea

# Time Complexity: O(n), since each element is pushed and popped from the stack at most once.
# Space Complexity: O(n), due to the additional arrays `leftMost` and `rightMost` and the stack.

