def reverseString(string):
    #Conditions: in-place, without using any predefined properties/functions to
    #            do reversing, without using additional variables
    #string is immutable in python - to reverse in place, we first convert the
    #string to a list
    string = list(string)
    
    left = 0
    right = len(string) - 1
    
    while left < right:
        #to reverse without new variables - use xor operation on the chars
        string[left] = ord(string[left]) ^ ord(string[right])
        string[right] = chr(string[left] ^ ord(string[right]))
        string[left] = chr(string[left] ^ ord(string[right]))
        left += 1
        right -= 1
    
    return "".join(string)


print(reverseString("hello"))
print(reverseString("hell"))
print(reverseString("holalalala"))
print(reverseString(""))