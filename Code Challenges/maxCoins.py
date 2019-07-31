#Challenge: You are given a 2-d matrix where each cell represents number of coins in that cell. 
#           Assuming we start at matrix[0][0], and can only move right or down, find the maximum 
#           number of coins you can collect by the bottom right corner.

def checkBound(max_row, max_col, row, col):
    return row >= 0 and row < max_row and col >= 0 and col < max_row

def maxCoins(matrix):
    max_row = len(matrix)
    max_col = len(matrix[0])
    for row_idx in range(max_row):
        for col_idx in range(max_col):
            top_val, right_val = 0, 0
            if checkBound(max_row, max_col, row_idx-1, col_idx):
                top_val = matrix[row_idx-1][col_idx]
            if checkBound(max_row, max_col, row_idx, col_idx-1):
                right_val = matrix[row_idx][col_idx-1]
            curr_val = matrix[row_idx][col_idx]
            matrix[row_idx][col_idx] = max(top_val+curr_val, right_val+curr_val)
    return matrix[max_row-1][max_col-1]

if __name__ == "__main__":
    print(maxCoins([[0,3,1,1],[2,0,0,4],[1,5,3,1]]))