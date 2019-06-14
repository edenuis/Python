#Challenge: Given an array C of size N-1 and given that there are numbers from 
#           1 to N with one element missing, the missing number is to be found.

#Idea: Using sum formula, we can find the total sum from 1 to N. Then minus
#      away all numbers in the array of numbers. Remaining sum is the answer.

def findMissingNumber(numbers):
    n = len(numbers) + 1
    total = n*(n + 1)/2
    for number in numbers:
        total -= number
    return int(total)

if __name__ == '__main__':
    assert findMissingNumber([1,2,3,5]) == 4
    assert findMissingNumber([1,2,3,4,5,6,7,8,10]) == 9
    assert findMissingNumber([5,2,3,7,6,4,1]) == 8
