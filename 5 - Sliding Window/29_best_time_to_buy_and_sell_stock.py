def maxProfit(prices):
    # Initialize max profit to 0
    maxP = 0
    # Left pointer for buying day
    l = 0
    # Right pointer for selling day
    r = 1  

    while True:
        # Check if pointers are out of bounds
        if l > len(prices) - 2 or r > len(prices) - 1:
            return maxP
        
        # Calculate potential profit
        profit = prices[r] - prices[l]
        
        # If the current profit is smaller than maxP and the next buying price is lower, shift both pointers
        if profit < maxP and prices[l + 1] < prices[l]:
            r += 1
            l += 1
        else:
            # Update max profit if the current profit is greater
            if profit > maxP:
                maxP = profit
            # If the selling price is lower than the buying price, move the buying pointer
            if prices[r] < prices[l]:
                l = r
                r = l + 1
            else:
                r += 1

# Time Complexity: O(n), where n is the number of prices. Each price is processed once.
# Space Complexity: O(1), since only a few variables are used.