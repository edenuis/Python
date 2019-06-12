#Challenge: You are given an N by M 2D matrix of lowercase letters. Determine 
#           the minimum number of columns that can be removed to ensure that 
#           each row is ordered from top to bottom lexicographically. That is, 
#           the letter at each column is lexicographically later as you go down 
#           each row. It does not matter whether each row itself is ordered 
#           lexicographically.

def getMinColsToDrop(matrix):
    if matrix == []:
        return 0
    if len(matrix) == 1:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for col_idx in range(cols):
        for row_idx in range(1, rows):
            if matrix[row_idx-1][col_idx] > matrix[row_idx][col_idx]:
                 count += 1
                 break
    return count

if __name__ == '__main__':
    assert getMinColsToDrop(["cba", "daf", "ghi"]) == 1
    assert getMinColsToDrop(["abcdef"]) == 0
    assert getMinColsToDrop(["zyx", "wvu", "tsr"]) == 3