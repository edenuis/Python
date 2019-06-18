#Quicksort

def partition(numbers, start, end):
    pivot = numbers[start]
    small_idx = start + 1
    for idx in range(start+1, end+1):
        if numbers[idx] < pivot:
            numbers[small_idx], numbers[idx] = numbers[idx], numbers[small_idx]
            small_idx += 1
    numbers[start], numbers[small_idx-1] = numbers[small_idx-1], numbers[start]
    return small_idx-1
        
def quickSort(numbers, start, end):
    if start < end:
        part_idx = partition(numbers, start, end)
        quickSort(numbers, start, part_idx-1)
        quickSort(numbers, part_idx+1, end)
    return numbers

if __name__ == "__main__":
    assert quickSort([1,2,3,4,5], 0, 4) == [1,2,3,4,5]
    assert quickSort([5,4,3,2,1], 0, 4) == [1,2,3,4,5]
    assert quickSort([5,2,3,4,4,2,1], 0, 6) == [1,2,2,3,4,4,5]
    assert quickSort([], 0, 0) == []
    assert quickSort([-1,23,0,123,5,6,4,-12], 0, 7) == [-12,-1,0,4,5,6,23,123]
    assert quickSort([10, 7, 8, 9, 1, 5], 0, 5) == [1,5,7,8,9,10]