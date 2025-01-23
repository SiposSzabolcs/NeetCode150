def productExceptSelf(nums):
    # Initialize result array with 1s
    res = [1] * (len(nums))
    
    # Compute prefix products
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    
    # Compute suffix products, combining with prefix products
    suffix = 1
    for i in range(len(nums) - 1, -1, -1):  # Traverse from last to first
        res[i] *= suffix
        suffix *= nums[i]
        
    return res
    
'''
Time Complexity: O(n), where n is the length of nums. 
- We traverse the array twice, once for prefix and once for suffix, but each element is processed only once in total.

Space Complexity: O(1) if we don't count the output array; otherwise, O(n).
- We only use a constant amount of extra space for 'prefix' and 'suffix'. 
- The 'res' array is considered part of the output, not additional space in terms of complexity analysis for this problem.
'''