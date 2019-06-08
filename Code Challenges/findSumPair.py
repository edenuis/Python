#Challenge 1: Given a list of numbers and a number k, return whether any two 
#             numbers from the list add up to k.

#Idea: One pass - Store past numbers in a dictionary

def findSumPair(numbers, k):
    num = {}
    
    for number in numbers:
        if k - number in num:
            return True
        else:
            num[number] = True
    return False

#Challenge 2: Similar to Challenge 1 but a sorted list is given

#Idea: Have two pointers - one at the start and one at the end of the list
#      If sum of numbers at both pointers is larger than k, move end pointer
#      down by one. Else, increase left pointer by 1.

def findSumPairSorted(numbers, k):
    l = 0
    r = len(numbers) - 1
    
    while l < r:
        total = numbers[l] + numbers[r]
        if total == k:
            return True
        elif total < k:
            l += 1
        else:
            r -= 1
    return False

#Challenge 3: Similar to Challenge 1 but print all possible pairs

#Idea: Just need to modify solution of Challenge 1 to print all pairs
    
def findAllSumPair(numbers, k):
    num = {}
    
    allPairs = []
    for number in numbers:
        if k - number in num:
            allPairs.append((number, k - number))
        else:
            num[number] = True
    return allPairs

if __name__ == '__main__':
    print(findSumPair([10, 15, 3, 7], 19))
    print(findSumPair([10, 15, 3, 7], 17))
    
    print(findSumPairSorted([3, 7, 10, 15], 17))
    print(findSumPairSorted([3, 7, 10, 15, 20, 22, 50], 19))
    print(findSumPairSorted([3, 7, 10, 15, 20, 22, 50], 40))
    print(findSumPairSorted([3, 7, 10, 15, 20, 22, 50], 25))

    print(findAllSumPair([10, 15, 3, 7, 12, 11, 8, 6, 9], 19))
    print(findAllSumPair([10, 15, 3, 7, 12, 11, 8, 6, 9], 17))
    print(findAllSumPair([10, 15, 3, 7, 12, 11, 8, 6, 9], 100))