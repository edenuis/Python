#Challenge: Given an array A[] of N positive integers. The task is to find the 
#           maximum of j - i subjected to the constraint of A[i] <= A[j].

def processMin(numbers):
    min_set = [0]*len(numbers)
    curr_min = numbers[0]
    for idx in range(len(numbers)):
        if curr_min > numbers[idx]:
            curr_min = numbers[idx]
        min_set[idx] = curr_min
    return min_set

def processMax(numbers):
    max_set = [0]*len(numbers)
    curr_max = numbers[len(numbers)-1]
    for idx in range(len(numbers)-1, -1, -1):
        if curr_max < numbers[idx]:
            curr_max = numbers[idx]
        max_set[idx] = curr_max
    return max_set

def findMaximumIndex(numbers):
    min_set = processMin(numbers)
    max_set = processMax(numbers)
    min_idx = 0
    max_idx = 0
    max_diff = -1
    while min_idx < len(numbers) and max_idx < len(numbers):
        if max_set[max_idx] - min_set[min_idx] >= 0:
            max_diff = max(max_diff, max_idx - min_idx)
            max_idx += 1
        else:
            min_idx += 1
    return max_diff

if __name__ == "__main__":
    print(findMaximumIndex([34,8,10,3,2,80,30,33,1]))
    print(findMaximumIndex([5,4,3,2,1]))

