#Challenge: Give an array arr[] of N integers and another integer k ≤ N. The 
#           task is to find the maximum element of every sub-array of size k.

from collections import deque

def printMax(numbers, k):
    dq = deque()
    max_list = [None]*(len(numbers)-k+1)
    for idx in range(k):
        while dq and numbers[idx] >= numbers[dq[-1]]:
            dq.pop()
        dq.append(idx)
    for idx in range(k, len(numbers)):
        max_list[idx-k] = numbers[dq[0]]
        while dq and dq[0] <= idx - k:
            dq.popleft()
        while dq and numbers[idx] >= numbers[dq[-1]]:
            dq.pop()
        dq.append(idx)
    max_list[len(max_list)-1] = numbers[dq[0]]
    return max_list

if __name__ == '__main__':
    assert printMax([1,2,3,1,4,5,2,3,6], 3) == [3,3,4,5,5,5,6]
    assert printMax([8,5,10,7,9,4,15,12,90,13], 4) == [10,10,10,15,15,90,90]
    assert printMax([1,2,3,4,5,6,7,8,9,10], 5) == [5,6,7,8,9,10]