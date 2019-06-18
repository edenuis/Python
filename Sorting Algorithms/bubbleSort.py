#Bubble sort

def bubbleSort(numbers):
    while True:
        swap = False
        count = 1
        for idx in range(len(numbers)-count):
            if numbers[idx] > numbers[idx+1]:
                numbers[idx], numbers[idx+1] = numbers[idx+1], numbers[idx]
                swap = True
        if not swap:
            break
        count += 1
    return numbers

if __name__ == "__main__":
    assert insertionSort([1,2,3,4,5]) == [1,2,3,4,5]
    assert insertionSort([5,4,3,2,1]) == [1,2,3,4,5]
    assert insertionSort([5,2,3,4,4,2,1]) == [1,2,2,3,4,4,5]
    assert insertionSort([]) == []
    assert insertionSort([-1,23,0,123,5,6,4,-12]) == [-12,-1,0,4,5,6,23,123]