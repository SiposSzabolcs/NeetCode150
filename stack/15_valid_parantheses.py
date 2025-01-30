def isValid(s):
    # Stack to keep track of opening brackets
    stack = []
    # Mapping of closing brackets to their corresponding opening brackets
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        # If it's an opening bracket, push it onto the stack
        if char in mapping.values():
            stack.append(char)
        # If it's a closing bracket, check for a valid match
        elif char in mapping:
            # If the stack is empty or the top doesn't match, it's invalid
            if not stack or stack.pop() != mapping[char]:
                return False

    # If the stack is empty, all brackets were properly closed
    return not stack

# Space Complexity: O(n) - In the worst case, the stack holds all opening brackets.
# Time Complexity: O(n) - Each character is processed once.