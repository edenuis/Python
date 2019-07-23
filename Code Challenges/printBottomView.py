#Challenge: Given a binary tree, print the bottom view from left to right.
#           A node is included in bottom view if it can be seen when we look at 
#           the tree from bottom.

#Idea: Set an int variable that keeps track of the bottom-most node for each value.
#      For each value, we only want to keep the node that is of the highest
#      height value. Each time we traverse to the left side of the tree, we minus
#      1 from the current value. We then plus 1 for right side of the tree.
#      Use a dictionary to keep track of the values. The final state of the 
#      dictionary will give us the bottom view of the tree by printing from the
#      smallest to largest value.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def printBottomView(root):
    dic = {}
    start = processTree(root, dic, 0, 0, 0)
    string = ""
    for idx in range(start, start+len(dic)):
        string += str(dic[idx][1]) + " "
    return string.strip()

def processTree(root, dic, height, value, offset):
    if root is None:
        return value-offset
    if value in dic:
        if dic[value][0] < height:
            dic[value] = (height, root.value)
    else:
        dic[value] = (height, root.value)
    min_left_value = processTree(root.left, dic, height+1, value-1, -1)
    min_right_value = processTree(root.right, dic, height+1, value+1, 1)
    return min(min_left_value, min_right_value)

if __name__ == "__main__":
    root = Node(20)
    node2 = Node(8)
    node3 = Node(22)
    node4 = Node(5)
    node5 = Node(3)
    node6 = Node(25)
    node7 = Node(10)
    node8 = Node(14)
    
    root.left = node2
    root.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node6
    node5.left = node7
    node5.right = node8
    
    print(printBottomView(root))
    
    root = Node(1)
    node2 = Node(3)
    node3 = Node(2)
    root.left = node2
    root.right = node3
    print(printBottomView(root))