#Challenge: Count inversions in an array
#           Inversion Count for an array indicates – how far (or close) the 
#           array is from being sorted. If array is already sorted then 
#           inversion count is 0. If array is sorted in reverse order that 
#           inversion count is the maximum. 
#           Formally speaking, two elements a[i] and a[j] form an inversion if 
#           a[i] > a[j] and i < j

import math
def countInversions(numbers):
    size = math.ceil(len(numbers)/2)
    count = 0
    while size > 0:
        i = 0
        while i + size < len(numbers):
            if numbers[i] > numbers[i + size]:
                count += 1
            i += 1
        if size/2 < 1:
            break
        size = math.ceil(size/2)
    return count

if __name__ == '__main__':
    assert countInversions([2,4,1,3,5]) == 3
    assert countInversions([]) == 0
    assert countInversions([1,2,3,4,5]) == 0
    assert countInversions([3,2,1]) == 3
    assert countInversions([2,2,1,4,1]) == 4
    assert countInversions([1,20,6,4,5]) == 5
    assert countInversions([1]) == 0
    assert countInversions([1,2,3,4,2,3,4,5]) == 3