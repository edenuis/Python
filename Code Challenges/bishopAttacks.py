#Challenge: On our special chessboard, two bishops attack each other if they 
#           share the same diagonal. This includes bishops that have another 
#           bishop located between them, i.e. bishops can attack through pieces.
#           You are given N bishops, represented as (row, column) tuples on a 
#           M by M chessboard. Write a function to count the number of pairs of
#           bishops that attack each other. The ordering of the pair doesn't 
#           matter: (1, 2) is considered the same as (2, 1).

#Idea: Two bishops attack each other iff 
#      1) sum of coordinates are the same OR
#      2) difference of coordinates are the same

def attackPairs(bishops):
    coord_sum = {}
    coord_diff = {}
    
    count = 0
    for bishop in bishops:
        sum_coord = bishop[0] + bishop[1]
        diff_coord = bishop[0] - bishop[1]
        
        if sum_coord not in coord_sum:
            coord_sum[sum_coord] = 1
        else:
            count += coord_sum[sum_coord]
            coord_sum[sum_coord] += 1
            
        if diff_coord not in coord_diff:
            coord_diff[diff_coord] = 1
        else:
            count += coord_diff[diff_coord]
            coord_diff[diff_coord] += 1 
    return count

if __name__ == '__main__':
    m = int(input())
    n = int(input())
    
    bishops = []
    
    for i in range(n):
        x, y = input().split(' ')
        bishops.append((int(x), int(y)))
    print(bishops)   
    print(attackPairs(bishops))