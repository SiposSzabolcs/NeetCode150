def characterReplacement(s, k):
    # Dictionary to store the frequency of characters in the current window
    count = {}

    res = 0  # Stores the length of the longest valid substring
    l = 0  # Left pointer of the sliding window
    maxf = 0  # Max frequency of any single character in the window

    # Iterate through the string with the right pointer
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)  # Update character count
        maxf = max(maxf, count[s[r]])  # Track the most frequent character in the window

        # If the remaining characters in the window exceed `k` replacements, shrink the window
        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1  # Remove the leftmost character
            l += 1  # Move the left pointer to reduce the window size
        
        # Update the maximum valid substring length
        res = max(res, r - l + 1)

    return res

# Time Complexity: O(n)
# - Each character is processed at most twice (once when expanding, once when shrinking).
# - The while loop ensures an amortized O(n) time complexity.

# Space Complexity: O(26) ≈ O(1)
# - The count dictionary stores at most 26 unique English letters, making it effectively O(1).
# - If extended character sets are used, worst-case space complexity is O(n).
