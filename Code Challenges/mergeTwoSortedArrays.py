#Challenge: Given two sorted arrays, we need to merge them in O((n+m)*log(n+m)) 
#           time with O(1) extra space into a sorted array, when n is the size 
#           of the first array, and m is the size of the second array.

import math

def mergeTwoSortedArrays(items_1, items_2):
    size = math.ceil((len(items_1)+len(items_2))/2)
    while size > 0:
        i = 0
        while i + size < len(items_1):
            if items_1[i] > items_1[i + size]:
                tmp = items_1[i]
                items_1[i] = items_1[i + size]
                items_1[i + size] = tmp
            i += 1
        while i < len(items_1) and i + size - len(items_1) < len(items_2):
            if items_1[i] > items_2[i + size - len(items_1)]:
                tmp = items_1[i]
                items_1[i] = items_2[i + size - len(items_1)]
                items_2[i + size - len(items_1)] = tmp
            i += 1
        while i - len(items_1) < len(items_2) and i + size - len(items_1) < len(items_2):
            if items_2[i - len(items_1)] > items_2[i + size - len(items_1)]:
                tmp = items_2[i - len(items_1)]
                items_2[i - len(items_1)] = items_2[i + size - len(items_1)]
                items_2[i + size - len(items_1)] = tmp
            i += 1
        if size/2 < 1:
            break
        size = math.ceil(size/2)
    return items_1, items_2

if __name__ == '__main__':
    print(mergeTwoSortedArrays([10], [2,3]))
    print(mergeTwoSortedArrays([1,5,9,10,15,20], [2,3,8,13]))
    print(mergeTwoSortedArrays([1,2,3], [4,5,6,7]))
    print(mergeTwoSortedArrays([1,2,3], [2,3,4]))
    print(mergeTwoSortedArrays([5,4,3], [2,1]))
    print(mergeTwoSortedArrays([], [2,1,4,2,5,6,7]))
    print(mergeTwoSortedArrays([3,4,6,7], []))