#Challenge: Chocolate Distribution Problem

#Idea: If the chocolate packets are sorted based on the amount of chocolates it 
#      contains, then the problem will be simplified to checking which window
#      of chocolate packets has the smallest difference between the largest
#      and the smallest amount of chocolates. 
from math import ceil

def mergeSort(items):
    max_len = ceil(len(items)/2)
    while max_len >= 1:
        start = 0
        while start + max_len < len(items):
            if items[start] > items[start+max_len]:
                items[start], items[start+max_len] = items[start+max_len], items[start]
            start += 1
        if max_len == 1:
            break
        max_len = ceil(max_len/2)

def minDiff(items, k):
    mergeSort(items)
    print(items)
    min_diff = items[-1]
    start = 0
    while start + k - 1< len(items):
        min_diff = min(min_diff, items[start+k-1]-items[start])
        start += 1
    return min_diff

if __name__ == "__main__":
    print(minDiff([1,2,3,4,5,6], 3))
    print(minDiff([6,5,4,3,2,1], 3))
    print(minDiff([1,1,1,1,1,1], 3))
    print(minDiff([2,5,3,1,4,6], 3))
    print(minDiff([2,5,3,1,4,6,2,3], 3))
    print(minDiff([3,4,1,9,56,7,9,12], 5))
    print(minDiff([7,3,2,4,9,12,6], 3))

    
    
    
    
    
    