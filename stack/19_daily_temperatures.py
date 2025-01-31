def dailyTemperatures(temperatures):
    # Initialize output array with zeros
    out = [0] * len(temperatures)
    stack = []  # Monotonic decreasing stack (stores indices)
    
    # Iterate through temperatures
    for i, temp in enumerate(temperatures):
        # Process the stack while there are smaller temperatures
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()
            out[prev_index] = i - prev_index
        
        # Store the current index in the stack
        stack.append(i)
    
    return out

# Time Complexity: O(n), since each element is pushed and popped from the stack at most once.
# Space Complexity: O(n), for storing the output array and the stack in the worst case.
