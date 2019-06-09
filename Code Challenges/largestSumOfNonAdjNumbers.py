#Challenge 1: Given a list of integers, write a function that returns the largest 
#           sum of non-adjacent numbers. Numbers can be 0 or negative. For 
#           example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 
#           5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

#Idea: Max sum is the maximum of (1) and (2):
#      (1) Max sum including the element pointed by current index
#      (2) Max sum excluding the element pointed by current index 
def largestSum(numbers):
    if len(numbers) == 0:
        return 0
    elif len(numbers) <= 2:
        return max(numbers)
    dic = {len(numbers) - 1: numbers[len(numbers) - 1], 
           len(numbers) - 2: max(numbers[len(numbers)-2], numbers[len(numbers)-1])
           }
    for idx in range(len(numbers)-3, -1, -1):
        dic[idx] = max(numbers[idx] + dic[idx+2], dic[idx+1])
    return dic[0]

#Challenge 2: Same as Challenge 1 but O(1) space complexity
#Idea: Recursively (or iteratively) check the largest number including and excluding a number.
#      Return the max of both
def largestSum2(numbers):
    if len(numbers) == 0:
        return 0
    elif len(numbers) <= 2:
        return max(numbers)
    incl = 0
    excl = 0
    for idx in range(len(numbers)):
        temp = incl
        incl = max(excl + numbers[idx], incl)
        excl = temp
    return excl if excl > incl else incl

def largestSum3(numbers):
    if len(numbers) == 0:
        return 0
    elif len(numbers) <= 2:
        return max(numbers)
    
    including = largestSum3(numbers[2:]) + numbers[0]
    excluding = largestSum3(numbers[1:])
    return max(including, excluding)

if __name__ == '__main__':
    print(largestSum([2, 4, 6, 2, 5]))
    print(largestSum([5, 1, 1, 5]))
    print(largestSum([-55, -1, 1, 1, 5]))
    print(largestSum([5, 5, 10, 100, 10, 5]))
    print("==================================")
    print(largestSum2([2, 4, 6, 2, 5]))
    print(largestSum2([5, 1, 1, 5]))
    print(largestSum2([-55, -1, 1, 1, 5]))
    print(largestSum2([5, 5, 10, 100, 10, 5]))
    print("==================================")
    print(largestSum3([2, 4, 6, 2, 5]))
    print(largestSum3([5, 1, 1, 5]))
    print(largestSum3([-55, -1, 1, 1, 5]))
    print(largestSum3([5, 5, 10, 100, 10, 5]))
    
