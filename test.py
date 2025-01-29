board = [["1","2",".",".","3",".",".",".","."],
         ["4",".",".","5",".",".",".",".","."],
         [".","9","8",".",".",".",".",".","3"],
         ["5",".",".",".","6",".",".",".","4"],
         [".",".",".","8",".","3",".",".","5"],
         ["7",".",".",".","2",".",".",".","6"],
         [".",".",".",".",".",".","2",".","."],
         [".",".",".","4","1","9",".",".","8"],
         [".",".",".",".","8",".",".","7","9"]]


curr = board[0:3]

#print(curr[0][0:3])
#print(curr[1][0:3])
#print(curr[2][0:3])
#
#print(curr[0][3:6])
#print(curr[1][3:6])
#print(curr[2][3:6])
#
#print(curr[0][6:9])
#print(curr[1][6:9])
#print(curr[2][6:9])

def isValid(list):
    values = [x for x in list if x != "."]
    return len(values) == len(set(values))

def valid_3x3s(board):
    for i in range(0, 9, 3):  # Iterate over each 3x3 subgrid row-wise
        for j in range(0, 9, 3):  # Iterate over each 3x3 subgrid column-wise
            # Flatten the current 3x3 subgrid into a list
            submatrix = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            print(submatrix)
            # Check if the subgrid is valid
            if not isValid(submatrix):
                return False
    return True

print(valid_3x3s(board))
    