#Challenge: Given an array of both positive and negative integers, the task is 
#           to compute sum of minimum and maximum elements of all sub-array of 
#           size k.

from collections import deque

def sumMinAndMaxOfSubarraysWithK(numbers, k):
    min_dq = deque()
    max_dq = deque()
    count = 0
    for idx in range(k):
        while max_dq and numbers[idx] >= numbers[max_dq[-1]]:
            max_dq.pop()
        while min_dq and numbers[idx] <= numbers[min_dq[-1]]:
            min_dq.pop()
        max_dq.append(idx)
        min_dq.append(idx)
    for idx in range(k, len(numbers)):
        count += numbers[max_dq[0]] + numbers[min_dq[0]]
        while max_dq and max_dq[0] <= idx - k:
            max_dq.popleft()
        while min_dq and min_dq[0] <= idx - k:
            min_dq.popleft()
        while max_dq and numbers[idx] >= numbers[max_dq[-1]]:
            max_dq.pop()
        while min_dq and numbers[idx] <= numbers[min_dq[-1]]:
            min_dq.pop()
        max_dq.append(idx)
        min_dq.append(idx)
    count += numbers[max_dq[0]] + numbers[min_dq[0]]
    return count

if __name__ == '__main__':
    assert sumMinAndMaxOfSubarraysWithK([2,5,-1,7,-3,-1,-2], 4) == 18
    assert sumMinAndMaxOfSubarraysWithK([2,5,-1,7,-3,-1,-2], 3) == 14
    assert sumMinAndMaxOfSubarraysWithK([1,2,3,4,5,6], 6) == 7
    assert sumMinAndMaxOfSubarraysWithK([1,-2,3,-4,5,6], 6) == 2
    assert sumMinAndMaxOfSubarraysWithK([1,-2,3,-4,5,6], 4) == 2