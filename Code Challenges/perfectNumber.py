def perfectNum(n):
    count = 1
    start = 19
    
    while count < n:
        start += 9
        if start % 10 != 0:
            count += 1
        
    return start

print(perfectNum(1))
print(perfectNum(2))
print(perfectNum(3))
print(perfectNum(4))
print(perfectNum(5))
print(perfectNum(6))