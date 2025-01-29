def threeSum(numbers):
    # Sort the input list to facilitate the two-pointer approach
    numbers.sort()
    out = []

    # Iterate through the numbers, treating each as a potential first element
    for i in range(len(numbers) - 2):
        # Skip duplicate numbers to avoid duplicate triplets
        if i > 0 and numbers[i] == numbers[i - 1]:
            continue

        left = i + 1
        right = len(numbers) - 1

        while left < right:
            total = numbers[i] + numbers[left] + numbers[right]

            # If the sum is zero, add the triplet to the output list
            if total == 0:
                out.append([numbers[i], numbers[left], numbers[right]])

                # Skip duplicate elements to prevent duplicate triplets
                while left < right and numbers[left] == numbers[left + 1]:
                    left += 1
                while left < right and numbers[right] == numbers[right - 1]:
                    right -= 1

                # Move both pointers inward after finding a valid triplet
                left += 1
                right -= 1

            # If the sum is too small, move the left pointer to increase it
            elif total < 0:
                left += 1
            # If the sum is too large, move the right pointer to decrease it
            else:
                right -= 1

    return out

# Space Complexity: O(n) - Sorting requires O(n) space in some implementations, and the output list can store up to O(n) triplets.
# Time Complexity: O(n^2) - The outer loop runs O(n) times, and the two-pointer approach takes O(n) per iteration.
