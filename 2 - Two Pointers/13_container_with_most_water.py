def maxArea(heights):
    l = 0
    r = len(heights)-1
    curr_max = 0
    
    while True:
        
        if l == r:
            return curr_max
        
        curr = (r-l) * min(heights[l], heights[r])
        
        print(heights[l], heights[r])
        
        if curr > curr_max:
            curr_max = curr
            
        if heights[l] > heights[r]:
            r -= 1
        elif heights[l] < heights[r]:
            l += 1
        elif heights[l] == heights[r] and l != r:
            r -= 1
            

print(maxArea([1,7,2,5,12,3,500,500,7,8,4,7,3,6]))