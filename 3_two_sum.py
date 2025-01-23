def twoSum(numList, target):
    l = 0
    r = 1
    
    while True:
        if numList[l] + numList[r] == target:
            return [l,r]
        
        if r < len(numList)-1:
            r += 1
        else:
            l += 1
            r = l+1
        
    


print(twoSum([3,4,5,6], 11))