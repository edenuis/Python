#Challenge: Given an array arr of N integers. Find the contiguous sub-array 
#           with maximum sum.

#Idea: A contiguous subarray is the maximum if:
#      (1) Sum is positive and no smaller contiguous subarrays in the sum's 
#          subarray have a negative sum OR
#      (2) Sum is negative and no contiguous subarrays have sum is positve
#      Count the sum from left to right. If sum becomes negative, restart count.

def subarrayWithMaxSum(numbers):
    max_sum = None
    count = 0
    for number in numbers:
        count += number
        if max_sum is None or max_sum < count:
            max_sum = count
        if count < 0:
            count = 0
    return max_sum

if __name__ == '__main__':
    assert subarrayWithMaxSum([1,2,3,-2,5]) == 9
    assert subarrayWithMaxSum([-1,-2,-3,-4]) == -1
