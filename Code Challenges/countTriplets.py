#Challenge: Given an array of distinct integers. The task is to count all the 
#           triplets such that sum of two elements equals the third element.

#Idea: For each number in the array of integers, count the number of pairs of 
#      integers that adds to the number. Return the total count.

def countTripletsWithSumK(numbers, k):
    dic = {}
    count = 0
    for number in numbers:
        if k - number in dic:
            count += 1
        else:
            dic[number] = True
    return count

def countTriplets(numbers):
    count = 0
    for idx in range(len(numbers)):
        count += countTripletsWithSumK(numbers[:idx] + numbers[idx+1:], numbers[idx])
    return count if count > 0 else -1

if __name__ == '__main__':
    print(countTriplets([3,2,7]))
    print(countTriplets([1,5,3,2]))  
    print(countTriplets([1,3,4,15,19])) 
    print(countTriplets([7,2,5,4,3,6,1,9,10,12])) 