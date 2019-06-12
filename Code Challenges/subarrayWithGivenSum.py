#Challenge 1: Given an unsorted array of nonnegative integers, find a continous 
#           subarray which adds to a given number.

#Idea: Keep two pointers, left and right. Count the sum between left and right,
#      inclusively. If sum is larger than required, remove a number from the left
#      Else if sum is smaller than required, add a number to right. Stop when
#      sum is the desired number or when there are no more numbers to add to right.
def subarrayWithGivenSum(numbers, k):
    l = 0
    r = 0
    count = 0

    while r < len(numbers):
        count += numbers[r]
        r += 1
        if count > k:
            count -= numbers[l]
            l += 1
        if count == k:
            return l, r-1
    return -1

#Challenge 2: Given an unsorted array of integers, find a subarray which adds 
#             to a given number. If there are more than one subarrays with the 
#             sum as the given number, print any of them. 

def subarrayWithGivenSum2(numbers, k):
    dic = {}
    count = 0
    
    for idx in range(len(numbers)):
        count += numbers[idx]
        if count == k:
            return 0, idx
        if count - k in dic:
            return (dic[count - k]+1, idx)
        dic[count] = idx
    return -1

if __name__ == '__main__':
    print(subarrayWithGivenSum([15, 2, 4, 8, 9, 5, 10, 23], 23))
    print(subarrayWithGivenSum([1, 2, 3, 7, 5], 12))
    print(subarrayWithGivenSum([1, 2, 3, 7, 5], 55))
    print("==============================")
    print(subarrayWithGivenSum2([10, 2, -2, -20, 10], -10))
    print(subarrayWithGivenSum2([1, 4, 20, 3, 10, 5], 33))
    print(subarrayWithGivenSum2([-10, 0, 2, -2, -20, 10], 20))