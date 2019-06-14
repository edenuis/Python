#Challenge: Given an array of positive integers. Your task is to find the leaders 
#           in the array.
#           Note: An element of array is leader if it is greater than or equal 
#           to all the elements to its right side. Also, the rightmost element 
#           is always a leader. 

#Idea: Loop through the list from the right. Keep track of the curr_max at each
#      iteration. Print the leader if the curr_max is <= number at next index.

def findLeaders(numbers):
    string = str(numbers[len(numbers)-1])
    curr_max = numbers[len(numbers)-1]
    for idx in range(len(numbers)-2, -1, -1):
        if numbers[idx] >= curr_max:
            curr_max = numbers[idx]
            string = str(numbers[idx]) + " " + string
    return string

if __name__ == "__main__":
    assert findLeaders([16,17,4,3,5,2]) == "17 5 2"
    assert findLeaders([1,2,3,4,0]) == "4 0"
    assert findLeaders([7,4,5,7,3]) == "7 7 3"
    assert findLeaders([99,18,92,35,74,0,95,71,39,33,39,32,37,45,57,71,95,5,71,24,86,8,51,54,74,24,75,70,33,63,29,99,58,94]) == "99 99 94"
    