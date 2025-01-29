def isValidSudoku(board):
    def checkRows():
        # Check each row for validity. '.' represents an empty cell.
        for row in board:
            row = [i for i in row if i != "."]
            if not isValid(row):
                return False
        return True
    
    def checkCols():
        # Check each column for validity by transposing the board.
        for i in range(len(board[0])):
            curr = []
            for j in range(len(board)): 
                curr.append(board[j][i]) 
            if not isValid(curr): 
                return False
        return True
    
    def valid_3x3s():
        # Check each 3x3 sub-grid for validity
        for i in range(0, 9, 3):  # Start of each 3x3 grid row
            for j in range(0, 9, 3):  # Start of each 3x3 grid column
                # Flatten the 3x3 grid into a single list
                submatrix = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not isValid(submatrix):
                    return False
        return True
    
    def isValid(lst):
        # Check if the list contains duplicates, excluding '.' 
        values = [x for x in lst if x != "."]
        return len(values) == len(set(values))  # If length matches, no duplicates exist
    
    # Check if all conditions (rows, columns, and 3x3 sub-grids) are valid
    if checkRows() and checkCols() and valid_3x3s():
        return True
    
    return False

# Space Complexity: O(n) - Uses temporary lists of up to n elements where n is the board size dimension
# Time Complexity: O(n^2) - Each check involves going through each element of the board, which is n*n for an nxn board