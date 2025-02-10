def lengthOfLongestSubstring(s):
    # Set to store unique characters in the current window
    seen = set()
    l = 0  # Left pointer of the sliding window
    longest = 0  # Stores the length of the longest substring

    # Iterate through the string with the right pointer
    for r in range(len(s)):
        # Shrink window if a duplicate is found
        while s[r] in seen:
            seen.remove(s[l])  # Remove the leftmost character
            l += 1  # Move left pointer to shrink the window
        
        # Expand the window
        seen.add(s[r])
        longest = max(longest, r - l + 1)  # Update max substring length

    return longest

# Time Complexity: O(n)
# - Each character is processed at most twice (once when expanding, once when shrinking).
# - The while loop ensures an amortized O(n) time complexity.

# Space Complexity: O(min(n, 26)) ≈ O(1)
# - The set stores at most 26 unique English letters, making it effectively O(1).
# - In the worst case (extended character set), it could be O(n).
