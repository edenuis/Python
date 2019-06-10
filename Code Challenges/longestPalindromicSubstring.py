#Challenge: Given a string, find the longest substring which is palindrome.

def longestPalindromicSubstring(string):
    if string == '':
        return ''
    
    size = len(string)
    matrix = [[0]*size for i in range(size)]
    l_idx = 0
    r_idx = 0
    length = 1
    for idx in range(len(string)):
        matrix[idx][idx] = True
        if idx+1 < len(string) and string[idx] == string[idx+1]:
            matrix[idx][idx+1] = True
            if length < 2:
                length = 2
                l_idx = idx
                r_idx = idx + 1
        
    for i in range(2, len(string)):
        for j in range(0, len(string)-i):
            k = j+i
            
            if string[j] == string[k] and matrix[j+1][k-1]:
                matrix[j][k] = True
                if k - j + 1 > length:
                    length = k - j + 1
                    l_idx = j
                    r_idx = k
                 
    return string[l_idx:r_idx+1]

if __name__ == '__main__':
    print(longestPalindromicSubstring('forgeeksskeegfor'))
    print(longestPalindromicSubstring('abcdefghijklmnopqrstuvwxyz'))
    print(longestPalindromicSubstring(''))
    print(longestPalindromicSubstring('abbbba'))
    print(longestPalindromicSubstring('abba'))
            
            
            