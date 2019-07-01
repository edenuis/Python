#Challenge: Given an array arr[] of N non-negative integers representing height 
#           of blocks at index i as Ai where the width of each block is 1. 
#           Compute how much water can be trapped in between blocks after raining.

#Idea: Keep a stack of tuples: (wall_size, num_of_walls_btw)
#      Iterate through the wall sizes. For the current wall, calculate the amount
#      of water that can be stored at that current point. Store the current wall
#      into the stack.
 
def countRainWater(walls):
    stack = []
    amount = 0
    for idx in range(len(walls)):
        btw = 0
        curr_wall = walls[idx]
        count = 0
        last_wall = (0, 0)
        
        while stack != [] and stack[len(stack)-1][0] < curr_wall:
            last_wall = stack.pop()
            count += last_wall[0]*(last_wall[1]+1)
            btw += last_wall[1] + 1
            
        if stack == []:
            amount += last_wall[0] * btw - count
            btw = 0
        else:
            amount += curr_wall * btw - count
        stack.append((curr_wall, btw))
    return amount

if __name__ == "__main__":
    assert countRainWater([7,4,0,9]) == 10
    assert countRainWater([6,9,9]) == 0
    assert countRainWater([3,2,1]) == 0
    assert countRainWater([10,2,3,4,3,2,1,9]) == 39
    assert countRainWater([7,3,9,2,3,4,6,8]) == 21
    assert countRainWater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6