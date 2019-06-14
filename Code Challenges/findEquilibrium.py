#Challenge: Given an array A of N positive numbers. The task is to find the 
#           position where equilibrium first occurs in the array. Equilibrium 
#           position in an array is a position such that the sum of elements 
#           before it is equal to the sum of elements after it.

#Idea: Keep track of the right_sum and left_sum of a number(excluding) in the list.
#      Return the index of the number + 1 when right_sum = left_sum. Else, return -1
 
def findEquilibrium(numbers):
    left_sum = 0
    right_sum = 0
    
    for idx in range(len(numbers)-1, 0, -1):
        right_sum += numbers[idx]
    for idx in range(len(numbers)):
        if left_sum == right_sum:
            return idx + 1
        elif idx + 1 < len(numbers):
            left_sum += numbers[idx]
            right_sum -= numbers[idx+1]
    return -1

if __name__ == '__main__':
    assert findEquilibrium([1]) == 1
    assert findEquilibrium([1,3,5,2,2]) == 3
    assert findEquilibrium([1,3,5,2,1]) == -1
    