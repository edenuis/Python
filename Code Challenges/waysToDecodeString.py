#Challenge: Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
#           count the number of ways it can be decoded. For example, the 
#           message '111' would give 3, since it could be decoded as 'aaa', 
#           'ka', and 'ak'. You can assume that the messages are decodable. 
#           For example, '001' is not allowed.

#Idea: The number of ways to decode a string is the total of (1) + (2)
#      (1) number of ways to decode string[1:]
#      (2) number of ways to decode string[2:] if string[0:2] is in the range
#          of 1 - 26; Else, 0

#DP from right to left
def noOfWaysToDecode(string):
    #last digit in string always has 1 way to decode
    dic = {len(string) - 1: 1}
    for idx in range(len(string)-2, -1, -1):
        #Check if 2 digits are in range
        if int(string[idx] + string[idx+1]) > 26:
            #Not in range -> Only count ways for leftmost digit
            dic[idx] = dic[idx+1]
        #Else, 2 digits are in range. Need to check if index is out of bound
        elif idx+2 < len(string):
            dic[idx] = dic[idx+1] + dic[idx+2]
        else:
            dic[idx] = dic[idx+1] + 1
    return dic[0]


print(noOfWaysToDecode('111')) #3 ways
print(noOfWaysToDecode('4321')) #2 Ways - '4'+'3'+'2'+'1' or '4'+'3'+'21'
print(noOfWaysToDecode('4123')) #3 Ways - '4'+'1'+'2'+'3' or '4'+'1'+'23' or '4'+'12'+'3'
