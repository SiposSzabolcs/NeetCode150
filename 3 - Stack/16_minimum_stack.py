class MinStack:
    def __init__(self):
        # Stack to store all values
        self.stack = []
        # Stack to keep track of the minimum values
        self.min_stack = []

    def push(self, val: int) -> None:
        # Push value onto the main stack
        self.stack.append(val)
        
        # Push onto the min_stack if it's empty or the value is the new minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Remove the top element from the stack if it's not empty
        if self.stack:
            popped = self.stack.pop()
            # If the popped element is the current minimum, remove it from min_stack
            if popped == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        # Return the top element of the stack if it's not empty
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        # Return the minimum element from min_stack if it's not empty
        return self.min_stack[-1] if self.min_stack else None

# Space Complexity: O(n) - Each element is stored in both stack and min_stack in the worst case.
# Time Complexity: O(1) - Each operation (push, pop, top, getMin) runs in constant time.
