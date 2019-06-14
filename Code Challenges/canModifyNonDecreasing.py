#Challenge: Given an array of integers, write a function to determine whether 
#           the array could become non-decreasing by modifying at most 1 element.
#           For example, given the array [10, 5, 7], you should return true, 
#           since we can modify the 10 into a 1 to make the array non-decreasing.
#           Given the array [10, 5, 1], you should return false, since we can't 
#           modify any one element to get a non-decreasing array.

def canModify(numbers):
    curr_idx = -1
    for idx in range(1, len(numbers)):
        if numbers[idx] < numbers[idx-1]:
            if curr_idx is not -1:
                return False
            curr_idx = idx
    return curr_idx == -1 or curr_idx == 1 or curr_idx == len(numbers) - 1 or numbers[curr_idx-1] <= numbers[curr_idx+1] or numbers[curr_idx-2] <= numbers[curr_idx] 

if __name__ == '__main__':
    assert canModify([10, 5, 7])
    print("=======================")
    assert not canModify([10, 5, 1])
    print("=======================")
    assert canModify([1, 2, 3, 4, 5])
    print("=======================")
    assert canModify([1, 10, 2, 4, 5])
    print("=======================")
    assert canModify([1, 3, 2, 3, 5])
    print("=======================")
    assert not canModify([3, 4, 2, 3])