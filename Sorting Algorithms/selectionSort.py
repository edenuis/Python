#Selection sort

def selectionSort(numbers):
    for idx in range(1, len(numbers)):
        curr_idx = idx
        for sec_idx in range(idx-1, -1, -1):
            if numbers[curr_idx] >= numbers[sec_idx]:
                break
            numbers[curr_idx], numbers[sec_idx] = numbers[sec_idx], numbers[curr_idx]
            curr_idx = sec_idx
    return numbers
    
if __name__ == "__main__":
    assert insertionSort([1,2,3,4,5]) == [1,2,3,4,5]
    assert insertionSort([5,4,3,2,1]) == [1,2,3,4,5]
    assert insertionSort([5,2,3,4,4,2,1]) == [1,2,2,3,4,4,5]
    assert insertionSort([]) == []
    assert insertionSort([-1,23,0,123,5,6,4,-12]) == [-12,-1,0,4,5,6,23,123]