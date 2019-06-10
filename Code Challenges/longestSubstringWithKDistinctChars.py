#Challenge 1: Given an integer k and a string s, find the length of the longest 
#           substring that contains at most k distinct characters. For example, 
#           given s = "abcba" and k = 2, the longest substring with k distinct 
#           characters is "bcb".

#Idea: Keep two pointers on the string: left and right that tracks the current
#      string[left:right+1] being studied.
#      Keep a dictionary that stores the number of characters found
#      At every iteration, increase right pointer and check the number of 
#      distinct chars found. If number of distinct chars > k, increase left
#      pointer until there are only k distinct chars
def longestSubstring(string, k):
    if k == 0:
        return 0
    l = 0
    r = 0
    dic = {}
    count = 0 #track number of distinct chars in string[l: r+1]
    longest = 0 #track longest string found
    
    while r < len(string):
        if string[r] not in dic or dic[string[r]] == 0:
            dic[string[r]] = 1
            count += 1
        else:
            dic[string[r]] += 1
            
        while count > k:
            dic[string[l]] -= 1
            if dic[string[l]] == 0:
                count -= 1
            l += 1
        if count <= k and r - l + 1 > longest:
            longest = r - l + 1
        r += 1
    return longest

#Challenge 2: Similar to Challenge 1 but print all possible longest substring
def longestSubstring2(string, k):
    if k == 0:
        return None
    l = 0
    r = 0
    dic = {}
    count = 0 #track number of distinct chars in string[l: r+1]
    longest = 0 #track longest string found
    
    long_set = []
    while r < len(string):
        if string[r] not in dic or dic[string[r]] == 0:
            dic[string[r]] = 1
            count += 1
        else:
            dic[string[r]] += 1
            
        while count > k:
            dic[string[l]] -= 1
            if dic[string[l]] == 0:
                count -= 1
            l += 1
        if count <= k and r - l + 1 > longest:
            longest = r - l + 1
            long_set = []
            long_set.append((l, r))
        elif count <= k and r - l + 1 == longest:
            long_set.append((l, r))
        r += 1
    
    for x,y in long_set:
        print(string[x:y+1])
   
if __name__ == '__main__':
    print(longestSubstring("abcba", 1))
    print(longestSubstring("abcba", 2))
    print(longestSubstring("abcba", 3))
    print(longestSubstring("abcba", 4))
    print(longestSubstring("abcba", 0))
    print(longestSubstring("aabbcc", 2))
    print(longestSubstring("aabbcc", 1))
    print(longestSubstring("aaabbb", 3))
    print("=============================")
    longestSubstring2("abcba", 1)
    print("=============================")
    longestSubstring2("abcba", 2)
    print("=============================")
    longestSubstring2("abcba", 3)
    print("=============================")
    longestSubstring2("abcba", 4)
    print("=============================")
    longestSubstring2("abcba", 0)
    print("=============================")
    longestSubstring2("aabbcc", 2)
    print("=============================")
    longestSubstring2("aabbcc", 1)
    print("=============================")
    longestSubstring2("aaabbb", 3)
