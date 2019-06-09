#Challenge 1: Given an array of integers, return a new array such that each 
#             element at index i of the new array is the product of all the 
#             numbers in the original array except the one at i.

#Idea: One pass - Retrieve total product; Another pass to do division

def productList(numbers):
    total = 1
    
    for number in numbers:
        total *= number
    
    for idx in range(len(numbers)):
        numbers[idx] = int(total / numbers[idx])
    
    return numbers

#Challenge 2: Same as Challenge 1 but not allowed to use division
    
#Idea: Keep two lists - one list that keeps track of the product to the right of
#      number, another list to keep track of the product to the left of number.
    
def productList2(numbers):
    left = []
    right = []
    
    l = 0
    r = len(numbers) - 1
    l_prod = 1
    r_prod = 1
    for _ in range(len(numbers)):
        if l == 0:
            left.append(l_prod)
        else:
            l_prod *= numbers[l-1]
            left.append(l_prod)
        if r == len(numbers) - 1:
            right.append(r_prod)
        else:
            r_prod *= numbers[r+1]
            right.append(r_prod)
        l += 1
        r -= 1
    
    for idx in range(len(numbers)):
        numbers[idx] = left[idx] * right[len(numbers) - 1 - idx]
    return numbers

if __name__ == '__main__':
    print(productList([1, 2, 3, 4, 5]))
    print(productList2([1, 2, 3, 4, 5]))
    print(productList([]))
    print(productList([1]))