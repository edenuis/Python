#Merge sort

from math import ceil

def merge(numbers_1, numbers_2):
    ptr_1 = 0
    ptr_2 = 0
    numbers = []
    while ptr_1 < len(numbers_1) and ptr_2 < len(numbers_2):
        if numbers_1[ptr_1] <= numbers_2[ptr_2]:
            numbers.append(numbers_1[ptr_1])
            ptr_1 += 1
        else:
            numbers.append(numbers_2[ptr_2])
            ptr_2 += 1
    if ptr_1 < len(numbers_1):
        return numbers + numbers_1[ptr_1:]
    elif ptr_2 < len(numbers_2):
        return numbers + numbers_2[ptr_2:]
    return numbers

def mergeSort(numbers):
    if len(numbers) <= 1:
        return numbers
    size = ceil(len(numbers)/2)
    numbers_1 = mergeSort(numbers[:size])
    numbers_2 = mergeSort(numbers[size:])
    numbers = merge(numbers_1, numbers_2)
    return numbers

if __name__ == "__main__":
    assert mergeSort([1,2,3,4,5]) == [1,2,3,4,5]
    assert mergeSort([5,4,3,2,1]) == [1,2,3,4,5]
    assert mergeSort([5,2,3,4,4,2,1]) == [1,2,2,3,4,4,5]
    assert mergeSort([]) == []
    assert mergeSort([-1,23,0,123,5,6,4,-12]) == [-12,-1,0,4,5,6,23,123]