def evalRPN(tokens):
    stack = []
    
    for token in tokens:
        if token in {"+", "-", "*", "/"}:  # Operator found
            y, x = stack.pop(), stack.pop()  # Pop two operands
            match token:
                case "+":
                    stack.append(x + y)
                case "-":
                    stack.append(x - y)
                case "*":
                    stack.append(x * y)
                case "/":
                    stack.append(int(x / y))  # Ensure truncation towards zero
        else:
            stack.append(int(token))  # Push number to stack
    
    return stack[0]  # The final result is the only element left in the stack

# Test
print(evalRPN(["4", "13", "5", "/", "+"]))  # Expected Output: 6
