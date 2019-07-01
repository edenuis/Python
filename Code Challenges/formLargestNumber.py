#Challenge: Given a list of non negative integers, arrange them in such a manner 
#           that they form the largest number possible.The result is going to be 
#           very large, hence return the result in the form of a string.

def formLargestNumber(numbers):
    count = -1
    for idx in range(len(numbers)):
        if count < len(str(numbers[idx])):
            count = len(str(numbers[idx])) 
    
    for idx in range(len(numbers)):
        length = len(str(numbers[idx]))
        numbers[idx] = (str(numbers[idx])+"0"*(count-length), length)
    
    numbers = sorted(numbers, key=lambda x: x[0], reverse=True)
    
    string = ""
    for idx in range(len(numbers)):
        string += numbers[idx][0][0:numbers[idx][1]]
    return string

if __name__ == "__main__":
    assert formLargestNumber([3,30,34,5,9]) == "9534330"
    assert formLargestNumber([54,546,548,60]) == "6054854654"