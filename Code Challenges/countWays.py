#Challenge: There exists a staircase with N steps, and you can climb up either 
#           1 or 2 steps at a time. Given N, write a function that returns the 
#           number of unique ways you can climb the staircase. The order of the 
#           steps matters.

#Idea: Count the number of ways to do n-1 steps after taking 1 step + number of
#      ways to do n-2 steps after taking 2 step 
def countWays(n, dic={1:1, 2:2}):
    if n <= 0:
        return 0, dic
    elif n == 1:
        return 1, dic
    elif n == 2:
        return 2, dic
    elif n in dic:
        return dic[n], dic
    one_step, dic = countWays(n-1, dic)
    two_step, dic = countWays(n-2, dic)
    dic[n] = one_step + two_step
    return one_step + two_step, dic

#Challenge 2: What if, instead of being able to climb 1 or 2 steps at a time, 
#             you could climb any number from a set of positive integers X? 
#             For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps 
#             at a time.

#Idea: Same idea as in Challenge 1 - iteratively count the number of ways for 
#                                    each step and sum them up
def countWays2(n, steps, dic={1:1}):
    if n < 0:
        return 0, dic
    elif n == 1 or n == 0:
        return 1, dic
    elif n in dic:
        return dic[n], dic
    
    count = 0
    for step in steps:
        tmp, dic = countWays2(n-step, steps, dic)
        count += tmp
    dic[n] = count
    return count, dic

if __name__ == '__main__':
    print(countWays(0)[0]) #0 ways
    print(countWays(1)[0]) #1 way
    print(countWays(2)[0]) #2 ways - 1,1 or 2
    print(countWays(3)[0]) #3 ways - 1,1,1 or 1,2 or 2,1
    print(countWays(4)[0]) #5 ways - 1,1,1,1 or 1,1,2 or 1,2,1 or 2,1,1 or 2,2
    print(countWays(5)[0]) #8 ways - 1,1,1,1,1 or 1,1,1,2 or 1,1,2,1 or 1,2,1,1 or
                           #         2,1,1,1 or 1,2,2 or 2,1,2 or 2,2,1
    print("======================")
    print(countWays2(5, [1,3,5])) #3 ways - 1,1,1,1,1, 5, 3,1,1, 1,3,1, 1,1,3