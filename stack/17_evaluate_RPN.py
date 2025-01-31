def evalRPN(tokens):
    # Stack to store operands
    stack = []
    
    for token in tokens:
        if token in {"+", "-", "*", "/"}:  # Check if token is an operator
            y, x = stack.pop(), stack.pop()  # Pop the last two operands
            match token:
                case "+":  # Perform addition
                    stack.append(x + y)
                case "-":  # Perform subtraction
                    stack.append(x - y)
                case "*":  # Perform multiplication
                    stack.append(x * y)
                case "/":  # Perform division with truncation toward zero
                    stack.append(int(x / y))
        else:
            # Convert token to integer and push it to the stack
            stack.append(int(token))
    
    # The last remaining value in the stack is the final result
    return stack[0]

# Space Complexity: O(n) - In the worst case, all numbers are pushed onto the stack.
# Time Complexity: O(n) - Each token is processed once, with O(1) operations per token.
