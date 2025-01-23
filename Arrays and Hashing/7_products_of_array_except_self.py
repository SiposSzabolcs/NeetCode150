def productExceptSelf(nums):
    res = [1] * (len(nums))
    
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(len(nums) -1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
        
    return res
    
print(productExceptSelf([1,2,4,6]))