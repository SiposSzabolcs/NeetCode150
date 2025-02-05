import math

def minEatingSpeed(piles, h):
    # Search range: min speed = 1, max speed = largest pile
    l, r = 1, max(piles)
    # Start with max speed as the worst case
    minK = r  

    while l <= r:
        # Mid-point of binary search
        k = l + ((r - l) // 2)  
        # Total hours needed
        hours = sum(math.ceil(pile / k) for pile in piles)  

        if hours <= h:
            # Update the best found answer
            minK = k  
            # Try a smaller speed
            r = k - 1  
        else:
            # Increase speed
            l = k + 1  

    return minK

# Time Complexity: O(n log m), where n = len(piles) and m = max(piles)
# Space Complexity: O(1) (only a few integer variables are used)

