#Challenge: Given an array and a number k where k is smaller than size of array, 
#           we need to find the k’th smallest element in the given array. It is 
#           given that array elements are distinct.

#Idea: To modify quicksort algorithm to search for the kth smallest number
def partition(numbers, start, end):
    pivot = numbers[start]
    small_idx = start + 1
    for idx in range(start+1, end+1):
        if numbers[idx] < pivot:
            numbers[small_idx], numbers[idx] = numbers[idx], numbers[small_idx]
            small_idx += 1
    numbers[start], numbers[small_idx-1] = numbers[small_idx-1], numbers[start]
    return small_idx-1

def findKSmallestNumber(numbers, start, end, k):
    if start < end:
        pivot_idx = partition(numbers, start, end)
        if pivot_idx + 1 == k:
            return numbers[pivot_idx]
        elif pivot_idx + 1 > k:
            return findKSmallestNumber(numbers,start, pivot_idx-1, k)
        else:
            return findKSmallestNumber(numbers, pivot_idx+1, end, k)
            
if __name__ == "__main__":
    assert findKSmallestNumber([7,10,4,3,20,15], 0, 5, 3) == 7
    print("===================================")
    assert findKSmallestNumber([7,10,4,3,20,15], 0, 5, 4) == 10
    print("===================================")
    assert findKSmallestNumber([12,3,5,7,19], 0, 4, 2) == 5
    