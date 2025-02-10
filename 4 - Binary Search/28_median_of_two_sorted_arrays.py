def findMedianSortedArrays(nums1, nums2):
    # Assign the smaller array to A for efficiency
    A, B = nums1, nums2
    if len(B) < len(A):
        A, B = B, A

    total = len(A) + len(B)  # Total number of elements
    half = total // 2  # Midpoint index

    l, r = 0, len(A) - 1  # Binary search range in A

    while True:
        # i is the cut index for A, j is for B
        i = (l + r) // 2  
        j = half - i - 2  

        # Get left and right values from A and B, handling out-of-bounds cases
        Aleft = A[i] if i >= 0 else float("-infinity")
        Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
        Bleft = B[j] if j >= 0 else float("-infinity")
        Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

        # Check if partitioning is correct
        if Aleft <= Bright and Bleft <= Aright:
            # If total number of elements is odd, return the middle element
            if total % 2:
                return min(Aright, Bright)
            # If even, return the average of the two middle elements
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        
        # Adjust binary search range
        elif Aleft > Bright:
            r = i - 1  # Move left
        else:
            l = i + 1  # Move right

# Time Complexity: O(log(min(m, n))) where m and n are lengths of the input arrays
# Space Complexity: O(1) since only a few variables are used
