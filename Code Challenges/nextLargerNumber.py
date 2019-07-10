#Challenge: Given an array A of size N having distinct elements, the task is to 
#           find the next greater element for each element of the array in order 
#           of their appearance in the array. If no such element exists, output -1 

#Idea: Start from the back of the array. For each element, pop elements from the
#      stack only if the new element is larger than the popped element. Then the 
#      next larger element for the new element is the last element in stack.
#      Append the new element into step. Repeat the process till the end of array.
def convertString(items):
    string = ""
    for idx in range(len(items)):
        string += str(items[idx]) + " "
    return string

def nextLargerElement(numbers):
    stack = []
    next_larger = [None]*len(numbers)
    
    for idx in range(len(numbers)-1, -1, -1):
        num = numbers[idx]
        while stack != [] and stack[len(stack)-1] < num:
            stack.pop()
        if stack == []:
            next_larger[idx] = -1
        else:
            next_larger[idx] = stack[len(stack)-1]
        stack.append(num)
        
    return convertString(next_larger)

if __name__ == "__main__":
    assert nextLargerElement([1,3,2,4]) == "3 4 4 -1 "
    assert nextLargerElement([4,3,2,1]) == "-1 -1 -1 -1 "
    assert nextLargerElement([1,2,3,4,5,6,7,8]) == "2 3 4 5 6 7 8 -1 "
    