#Challenge: Given a number represented by a list of digits, find the next greater 
#           permutation of a number, in terms of lexicographic ordering. If there 
#           is not greater permutation possible, return the permutation with the 
#           lowest value/ordering.

def searchPivot(numbers):
    for idx in range(len(numbers)-1, 0, -1):
        if numbers[idx] > numbers[idx-1]:
            return idx
    return -1

def reverse(numbers):
    l = 0
    r = len(numbers)-1
    while l < r:
        numbers[l], numbers[r] = numbers[r], numbers[l]
        l += 1
        r -= 1
    return numbers

def nextLargerNumberIndex(numbers, start, number):
    for idx in range(len(numbers)-1, start-1, -1):
        if numbers[idx] > number:
            return idx
        
def nextGreaterArrangement(numbers):
    pivot = searchPivot(numbers)
    if pivot == -1:
        return reverse(numbers)
    index = nextLargerNumberIndex(numbers, pivot, numbers[pivot-1])
    numbers[pivot-1], numbers[index] = numbers[index], numbers[pivot-1]
    numbers[pivot:] = reverse(numbers[pivot:])
    return numbers

if __name__ == "__main__":
    assert nextGreaterArrangement([]) == []
    assert nextGreaterArrangement([1,2,3,4]) == [1,2,4,3]
    assert nextGreaterArrangement([1,4,7,100,99,94,23,12,1]) == [1,4,12,1,7,23,94,99,100]
    assert nextGreaterArrangement([3,2,1]) == [1,2,3]
    assert nextGreaterArrangement([1,3,2]) == [2,1,3]