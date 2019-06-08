#Challenge: Given a list of integers, return the largest product that can be 
#           made by multiplying any three integers.

#Idea: Given a sorted list of integers, the largest product will be formed by 
#      1) product of the 3 largest numbers OR
#      2) product of the 2 smallest numbers and the largest number

import sys
def largestProd(ints):
    l1 = -sys.maxsize
    l2 = -sys.maxsize
    l3 = -sys.maxsize
    s1 = sys.maxsize
    s2 = sys.maxsize
    
    if len(ints) == 0:
        return 0
    elif len(ints) <= 3:
        prod = 1
        for integer in ints:
            prod *= integer
        return prod
    
    for integer in ints:
        if integer >= l1:
            l3 = l2
            l2 = l1
            l1 = integer
        elif integer >= l2:
            l3 = l2
            l2 = integer
        elif integer > l3:
            l3 = integer
        
        if integer <= s2:
            s1 = s2
            s2 = integer
        elif integer < s1:
            s1 = integer
            
    return max(l1*l2*l3, s1*s2*l1)


print(largestProd([-10, -10, 5, 2]))
print(largestProd([]))
print(largestProd([1]))
print(largestProd([1,5]))
print(largestProd([4,7,9]))
print(largestProd([-20, -15, -10, 0, 1]))
print(largestProd([-20, 0, 1, 6]))
print(largestProd([-20, -15, -10, 0, 1, 9, 11]))
print(largestProd([-20, -15, -10, -9, -8, -7, -4]))
print(largestProd([20, 15, 10, 40, 1]))
            