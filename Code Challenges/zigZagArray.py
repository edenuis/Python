#Challenge: Given an array A (distinct elements) of size N. Rearrange the 
#           elements of array in zig-zag fashion. The converted array should be 
#           in form a < b > c < d > e < f. The relative order of elements is 
#           same in the output i.e you have to iterate on the original array 
#           only.

def swap(numbers, i, j):
    numbers[i], numbers[j] = numbers[j], numbers[i]
    
def zigZagArray(numbers):
    for idx in range(len(numbers)-1):
        if idx%2 == 0:
            if numbers[idx] > numbers[idx+1]:
                swap(numbers, idx, idx+1)
        else:
            if numbers[idx] < numbers[idx+1]:
                swap(numbers, idx, idx+1)
    return numbers

if __name__ == "__main__":
    assert zigZagArray([4,3,7,8,6,2,1]) == [3,7,4,8,2,6,1]
    assert zigZagArray([1,4,3,2]) == [1,4,2,3]
    assert zigZagArray([1,4,3,5,2,6]) == [1,4,3,5,2,6]