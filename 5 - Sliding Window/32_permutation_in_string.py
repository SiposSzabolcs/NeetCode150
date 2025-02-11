def checkInclusion(s1, s2):
    # Frequency array for lowercase letters (26 characters)
    char_count_s1 = [0] * 26
    char_count_s2 = [0] * 26
    
    # Fill frequency count for s1
    for char in s1:
        char_count_s1[ord(char) - ord('a')] += 1
    
    # Fill frequency count for the first window in s2
    for char in s2[:len(s1)]:
        char_count_s2[ord(char) - ord('a')] += 1
    
    # Check if initial window is a permutation
    if char_count_s1 == char_count_s2:
        return True

    # Sliding window
    l = 0
    for r in range(len(s1), len(s2)):
        char_count_s2[ord(s2[r]) - ord('a')] += 1  # Add new character
        char_count_s2[ord(s2[l]) - ord('a')] -= 1  # Remove old character
        l += 1  # Move window
        
        print(char_count_s1)
        print(char_count_s2)

        if char_count_s1 == char_count_s2:
            return True

    return False

# Example test
print(checkInclusion(s1="adc", s2="dcda"))

# Time Complexity: O(n)
# - Constructing `char_count_s1` takes O(m), where m = len(s1).
# - Constructing the initial `char_count_s2` takes O(m).
# - The sliding window runs O(n-m) times with O(1) updates per step.
# - Overall, O(m) + O(n-m) ≈ O(n).

# Space Complexity: O(1)
# - We only store two arrays of size 26 (constant space), so O(26) ≈ O(1).
