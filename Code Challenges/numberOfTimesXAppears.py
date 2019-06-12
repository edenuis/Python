#Challenge: Suppose you have a multiplication table that is N by N. That is, a 
#           2D array where the value at the i-th row and j-th column is 
#           (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).
#           Given integers N and X, write a function that returns the number of 
#           times X appears as a value in an N by N multiplication table.

#Idea: For 0<=i<=N-1, check if j is between 0 and N-1 (inclusive) and if j is
#      an integer. Calculate j using the formula: j = (X/(i+1)) - 1
def numberOfTimes(N, X):
    if X <= 0:
        return 0
    count = 0
    for i in range(N):
        j = (X/(i+1)) - 1
        if j >= 0 and j <= N-1 and (j*10)%10 == 0:
            count += 1
    return count

if __name__ == '__main__':
    print(numberOfTimes(6, -1)) #0 times
    print(numberOfTimes(6, 12)) #4 times
    print(numberOfTimes(6, 4)) #3 times
    print(numberOfTimes(6, 40)) #0 times
    print(numberOfTimes(6, 36)) #1 times