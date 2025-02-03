def generateParenthesis(n):
    # Stack to keep track of the current combination
    stack = []
    # Output list to store all valid parentheses combinations
    out = []
    
    def backtrack(openN, closedN):
        # Base case: if open and closed parentheses count reach 'n', add to result
        if openN == closedN == n:
            out.append("".join(stack))
            return
        
        # Add an opening parenthesis if we haven't used all 'n' yet
        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()
            
        # Add a closing parenthesis if we have more open than closed
        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()
            
    # Start backtracking with zero open and closed parentheses
    backtrack(0, 0)
    return out

# Space Complexity: O(n) - The recursion stack and list hold up to 'n' elements at a time.
# Time Complexity: O(2^n) - Each position has two choices, leading to an exponential number of calls.
