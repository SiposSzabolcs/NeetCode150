def searchMatrix(matrix,target):
            
    if matrix:
        for row in matrix:
            print(row)
            if row[-1] < target:
                pass
            elif row[-1] >= target:
                l = 0
                r = len(row) -1

                while l <= r:
                    m = l + ((r-l) // 2)
                    if row[m] > target:
                        r = m-1
                    elif row[m] < target:
                        l = m+1
                    else:
                        return True
                return False
        return False
    
print(searchMatrix([[1]],2))
