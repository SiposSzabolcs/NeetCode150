from collections import deque

def maxSlidingWindow(nums, k):
    q = deque()  # Stores indices of elements in decreasing order
    out = []
    
    for i in range(len(nums)):
        # Remove elements that are out of the window
        if q and q[0] < i - k + 1:
            q.popleft()  # O(1)

        # Remove elements that are smaller than the current element
        while q and nums[q[-1]] < nums[i]:
            q.pop()  # O(1) amortized
        
        # Add the current element's index
        q.append(i)  # O(1)
        
        # Add the max element to output once we reach size k
        if i >= k - 1:
            out.append(nums[q[0]])  # O(1)
    
    return out

# Time Complexity: O(n)
# - Each element is pushed and popped from the deque at most once.
# - The while loop ensures every element is processed in constant time on average.

# Space Complexity: O(k)
# - The deque stores at most `k` elements at a time.
