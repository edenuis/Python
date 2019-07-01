#Challenge: Given an unsorted array of size N. Find the first element in array 
#           such that all of its left elements are smaller and all right 
#           elements to it are greater than it.

def leftSmallerRightGreater(numbers):
    maximum = []
    minimum = []
    for idx in range(len(numbers)):
        if not maximum:
            maximum.append(numbers[idx])
        else:
            if maximum[len(maximum)-1] <= numbers[idx]:
                maximum.append(numbers[idx])
            else:
                maximum.append(maximum[len(maximum)-1])
                
        if not minimum:
            minimum.append(numbers[len(numbers)-1-idx])
        else:
            if minimum[len(minimum)-1] >= numbers[len(numbers)-1-idx]:
                minimum.append(numbers[len(numbers)-1-idx])
            else:
                minimum.append(minimum[len(minimum)-1])
    for idx in range(1, len(numbers)-1):
        if maximum[idx] == minimum[len(minimum)-1-idx]:
            return maximum[idx]
    return -1
    
if __name__ == "__main__":
    assert leftSmallerRightGreater([3,3,3,3]) == 3
    assert leftSmallerRightGreater([1,2,3,4]) == 2
    assert leftSmallerRightGreater([4,3,2,1]) == -1
    assert leftSmallerRightGreater([4,2,5,7]) == 5
    assert leftSmallerRightGreater([11,9,12]) == -1
    assert leftSmallerRightGreater([4,3,2,7,8,9]) == 7
