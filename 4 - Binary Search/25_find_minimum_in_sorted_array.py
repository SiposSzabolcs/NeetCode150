def findMin(nums):
    l,r = 0,len(nums)-1
    
    while l < r:
        m = l+((r-l) // 2)
        if nums[m] < nums[r]:
            r = m
        else:
            l = m+1
    
    return nums[l]
     
print(findMin([3,4,5,6,1,2]))    