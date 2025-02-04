def searchMatrix(matrix, target):
    # If the matrix is empty, return False
    if not matrix or not matrix[0]:
        return False
    
    for row in matrix:
        # If the last element of the row is smaller than the target, skip the row
        if row[-1] < target:
            continue
        
        # Apply binary search on the row
        l, r = 0, len(row) - 1
        while l <= r:
            m = l + (r - l) // 2  # Compute middle index
            if row[m] > target:
                r = m - 1  # Search left half
            elif row[m] < target:
                l = m + 1  # Search right half
            else:
                return True  # Target found
        
        return False  # If the target isn't in the row, return False early
    
    return False  # If the target isn't found in any row

# Time Complexity: O(m + log n) in the worst case, where m is the number of rows 
# and n is the number of columns. We iterate through the rows (O(m)), 
# and for one row, we perform binary search (O(log n)).

# Space Complexity: O(1) since we use only a few extra variables.