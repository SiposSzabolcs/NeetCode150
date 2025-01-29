def isPalindrome(string):
    # Remove non-alphanumeric characters and convert to lowercase
    string = [i.lower() for i in string if i.isalnum()]
    
    # If the string is empty after cleaning, it's considered a palindrome
    if len(string) == 0:
        return True
    
    l = 0
    r = len(string) - 1

    while True:
        # Check if the characters at the left and right pointers are the same
        if string[l] == string[r]:
            pass
        else:
            return False

        l += 1
        r -= 1

        # If the left pointer exceeds the right, the string is a palindrome
        if l > r:
            return True    

# Space Complexity: O(1) - We worked inplace on the string.
# Time Complexity: O(n) - We iterate through the string once to clean it and another time to check the characters.
