#Challenge: Given a binary tree, print the left view from top to bottom.
#           A node is included in left view if it can be seen when we look at 
#           the tree from the left.

#Idea: Set an int variable that keeps track of the left-most node for each height.
#      For each height, we only want to keep the node that is of the lowest 
#      value. Each time we traverse to the left side of the tree, we minus
#      1 from the current value. We then plus 1 for right side of the tree.
#      Use a dictionary to keep track of the height. The final state of the 
#      dictionary will give us the left view of the tree by printing from the
#      top to bottom.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def printLeftView(root):
    dic = {}
    max_height = processTree(root, dic, 0, 0)
    string = ""
    for idx in range(max_height+1):
        string += str(dic[idx][1]) + " "
    return string.strip()

def processTree(root, dic, height, value):
    if root is None:
        return height-1
    if height in dic:
        if dic[height][0] > value:
            dic[height] = (value, root.value)
    else:
        dic[height] = (value, root.value)
    max_left_height = processTree(root.left, dic, height+1, value-1)
    max_right_height = processTree(root.right, dic, height+1, value+1)
    return max(max_left_height, max_right_height)

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
    
    print(printLeftView(root))
    
    root = Node(1)
    node2 = Node(3)
    node3 = Node(2)
    root.left = node2
    root.right = node3
    print(printLeftView(root))