#Challenge: Given an array A of size N containing 0s, 1s, and 2s; you need to 
#           sort the array in ascending order.

#Idea 1: Count the number of 0s, 1s and 2s. Then create a new array of 0, 1 & 2.
def sortZerosOnesAndTwos(numbers):
    zeros = 0
    ones = 0
    twos = 0
    for number in numbers:
        if number == 0:
            zeros += 1
        elif number == 1:
            ones += 1
        else:
            twos += 1
    return [0]*zeros + [1]*ones + [2]*twos

#Idea 2:
def sortZerosOnesAndTwos2(numbers):
    i = 0
    j = len(numbers) - 1
    while i < len(numbers) and numbers[i] == 0:
        i += 1
    while j >= 0 and numbers[j] == 2:
        j -= 1
    for idx in range(i, j+1):
        if idx >= j+1:
            break
        tmp = numbers[idx]
        if tmp == 0:
            numbers[idx] = numbers[i]
            numbers[i] = tmp
            i += 1
        elif tmp == 2:
            if numbers[j] == 0:
                numbers[idx] = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = tmp
                i += 1
                j -= 1
            else:
                numbers[idx] = numbers[j]
                numbers[j] = tmp
                j -= 1
    return numbers

if __name__ == '__main__':
    assert sortZerosOnesAndTwos([0,2,1,1,0,2]) == [0,0,1,1,2,2]
    assert sortZerosOnesAndTwos([]) == []
    assert sortZerosOnesAndTwos([1,1,2,2]) == [1,1,2,2]
    assert sortZerosOnesAndTwos([2,2,1,1,0,0]) == [0,0,1,1,2,2]
    assert sortZerosOnesAndTwos([0,1,0]) == [0,0,1]
    assert sortZerosOnesAndTwos([0,2,1,2,0]) == [0,0,1,2,2]
    print("=================================")
    assert sortZerosOnesAndTwos2([0,2,1,1,0,2]) == [0,0,1,1,2,2]
    assert sortZerosOnesAndTwos2([]) == []
    assert sortZerosOnesAndTwos2([1,1,2,2]) == [1,1,2,2]
    assert sortZerosOnesAndTwos2([2,2,1,1,0,0]) == [0,0,1,1,2,2]
    assert sortZerosOnesAndTwos2([0,1,0]) == [0,0,1]
    assert sortZerosOnesAndTwos2([0,2,1,2,0]) == [0,0,1,2,2]
    