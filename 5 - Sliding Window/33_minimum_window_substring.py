def minWindow(s, t):
    if not s or not t:
        return ""

    # Create frequency dictionaries for t and the current window
    t_count = {}
    for char in t:
        t_count[char] = t_count.get(char, 0) + 1  # Count occurrences of characters in t

    window_count = {}  # Keeps track of characters in the current window
    have, need = 0, len(t_count)  # `need` is the number of unique characters in t that must match
    l, r = 0, 0
    res, res_len = [-1, -1], float("inf")

    while r < len(s):
        # Expand the window by adding s[r]
        char = s[r]
        window_count[char] = window_count.get(char, 0) + 1

        # If the count of char in window matches that in t, we count it as a match
        if char in t_count and window_count[char] == t_count[char]:
            have += 1

        # If all required characters are matched, try to shrink the window
        while have == need:
            # Update result if the current window is smaller
            if (r - l + 1) < res_len:
                res = [l, r]
                res_len = r - l + 1
            
            # Shrink from the left
            window_count[s[l]] -= 1
            if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                have -= 1
            l += 1

        r += 1

    l, r = res
    return s[l:r+1] if res_len != float("inf") else ""

# Time Complexity: O(n)
# - The `while r < len(s)` loop runs at most `n` times.
# - The inner `while have == need:` loop runs at most `n` times in total (since l and r both only move forward).
# - Thus, overall O(2n) ≈ O(n).

# Space Complexity: O(m)
# - The dictionaries `t_count` and `window_count` store at most `m` unique characters, where `m = len(t)`.
# - So, O(m) extra space is used.
