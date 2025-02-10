def maxProfit(prices):
    maxP = 0
    l = 0
    r = l+1
    
    while True:
        
        if l > len(prices) - 2 or r > len(prices) - 1:
            return maxP
        
        profit = prices[r]-prices[l]
        
        if profit < maxP and prices[l+1] < prices[l]:
            r += 1
            l += 1
        else:
            if profit > maxP:
                maxP = profit
            if prices[r] < prices[l]:
                l = r
                r = l+1
            else:
                r += 1

            
        

print(maxProfit([10,1,5,6,7,1]))