#Insertion sort

def insertionSort(numbers):
    for idx in range(len(numbers)-1):
        new_idx = idx
        for sec_idx in range(idx+1, len(numbers)):
            if numbers[sec_idx] < numbers[new_idx]:
                new_idx = sec_idx
        if new_idx != idx:
            numbers[idx], numbers[new_idx] = numbers[new_idx], numbers[idx]
    return numbers
    
if __name__ == "__main__":
    assert insertionSort([1,2,3,4,5]) == [1,2,3,4,5]
    assert insertionSort([5,4,3,2,1]) == [1,2,3,4,5]
    assert insertionSort([5,2,3,4,4,2,1]) == [1,2,2,3,4,4,5]
    assert insertionSort([]) == []
    assert insertionSort([-1,23,0,123,5,6,4,-12]) == [-12,-1,0,4,5,6,23,123]