#Merge Sort with O(1) space
import math

def mergeSort(items):
    size = math.ceil(len(items)/2)
    while size > 0:
        i = 0
        while i + size < len(items):
            if items[i] > items[i + size]:
                tmp = items[i]
                items[i] = items[i + size]
                items[i + size] = tmp
            i += 1
        if size/2 < 1:
            break
        size = math.ceil(size/2)
    return items

if __name__ == '__main__':
    print(mergeSort([1,2,3,4,5,6]))
    print(mergeSort([6,5,4,3,2,1]))
    print(mergeSort([1,1,1,1,1,1]))
    print(mergeSort([2,5,3,1,4,6]))
    print(mergeSort([2,5,3,1,4,6,2,3]))
    print(mergeSort([]))