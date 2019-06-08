#Challenge: Search in a row wise and column wise sorted matrix

#Solution: Start search from top right corner of the matrix. 

#          If value is greater than element, then the entire column can be 
#          ignored since all other values (below the indexed value) in the 
#          column will be greater than the element -> reduce search column index

#          If value is smaller than element, then the entire row can be ignored
#          since all other values (to the left of the indexed value) in the row
#          will be smaller than the element -> increase search row index

def search(matrix, elem):
    max_len = len(matrix)
    row = 0
    col = len(matrix) - 1
    
    while row < max_len and col >= 0:
        if matrix[row][col] == elem:
            return (row, col)
        elif matrix[row][col] > elem:
            col -= 1
        else:
            row += 1
    return "Not Found"


print(search([[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]], 29))
print(search([[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]], 100))
print(search([], 100))