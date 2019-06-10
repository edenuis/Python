#Challenge: Given a string of size n. The task is to find the length of the 
#           largest substring which is not palindrome.

#Idea: Check if string is make up of only one char. If yes, then length of 
#      longest non palindromic substring is 1. 
#      Else, check is string is palindrome. If no, then longest is n. Else, n-1
def isPalindrome(string):
    l = 0
    r = len(string) - 1
    while l < r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True

def longestNonPalindrome(string):
    if string == '':
        return 0
    
    count = 1
    char = string[0]
    for idx in range(1, len(string)):
        if string[idx] != char:
            break
        count += 1
        if count == len(string):
            return 1
        
    if isPalindrome(string):
        return len(string) - 1
    return len(string)

if __name__ == '__main__':
    print(longestNonPalindrome("abba"))
    print(longestNonPalindrome("aaaaa"))