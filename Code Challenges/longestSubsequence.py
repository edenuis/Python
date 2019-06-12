#Challenge: Given an array of numbers, find the length of the longest increasing 
#           subsequence in the array. The subsequence does not necessarily 
#           have to be contiguous.

def longestSubsequence(numbers):
    longest_ss_list = [1]*len(numbers)
    
    for idx in range(len(numbers)):
        for idx_ss in range(0, idx):
            if numbers[idx] > numbers[idx_ss] and longest_ss_list[idx] < longest_ss_list[idx_ss] + 1:
                longest_ss_list[idx] = longest_ss_list[idx_ss] + 1
    
    longest_ss = 0
    for length in longest_ss_list:
        longest_ss = max(longest_ss, length)
    return longest_ss
    
if __name__ == '__main__':
    print(longestSubsequence([1, 2, 3, 4, 5, 6, 7]))
    print(longestSubsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
    print(longestSubsequence([]))
    print(longestSubsequence([2, 3, 1]))
    print(longestSubsequence([2, 1, 0]))