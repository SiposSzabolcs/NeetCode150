def twoSum(numbers, target):
    l = 0
    r = len(numbers) - 1

    while True:
        # If the sum of the two numbers equals the target, return their 1-based indices
        if numbers[l] + numbers[r] == target:
            return [l + 1, r + 1]

        # If the sum is greater than the target, move the right pointer left
        if numbers[l] + numbers[r] > target:
            r -= 1

        # If the sum is smaller than the target, move the left pointer right
        if numbers[l] + numbers[r] < target:
            l += 1

        # If the pointers meet, there is no valid pair
        if l == r:
            return False

# Space Complexity: O(1) - Uses only two pointers, no additional data structures.
# Time Complexity: O(n) - In the worst case, each number is checked once as pointers move inward.
