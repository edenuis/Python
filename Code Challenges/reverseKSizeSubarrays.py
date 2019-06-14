#Challenge: Given an array arr[] of positive integers of size N. Reverse every 
#           sub-array of K group elements.

#Idea: Keep a window of size k. Sort the window whenever there are k elements or
#      if there are no more elements to add to the window and size < k.
#      Shift window to start from the previous end_index + 1
def reverse(numbers, i, j):
    if j >= len(numbers):
        j = len(numbers)
    l = i
    r = j-1
    while l < r:
        numbers[l], numbers[r] = numbers[r], numbers[l]
        l += 1
        r -= 1
    
def reverseKSizeSubarrays(numbers, k):
    start = 0
    while start < len(numbers):
        reverse(numbers, start, start + k)
        start = start + k
    return numbers

if __name__ == '__main__':
    assert reverseKSizeSubarrays([1,2,3,4,5], 3) == [3,2,1,5,4]
    assert reverseKSizeSubarrays([10,20,30,40,50,60], 2) == [20,10,40,30,60,50]
    