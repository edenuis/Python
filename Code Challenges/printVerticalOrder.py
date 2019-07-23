#Challenge: Print binary tree in vertical order

import queue

class Node: 
    def __init__(self, data): 
        self.value = data 
        self.left = None
        self.right = None
        
def printVerticalOrder(root):
    dic = {}
    start = processTree(root, dic, 0)
    for idx in range(start, start+len(dic)):
        printString(dic[idx])

def processTree(root, dic, value):
    q = queue.Queue()
    q.put((value, root))
    min_val = value
    while not q.empty():
        val, node = q.get()
        if val not in dic:
            dic[val] = []
        dic[val].append(node.value)
        
        if node.left is not None:
            q.put((val-1, node.left))
        if node.right is not None:
            q.put((val+1, node.right))
        min_val = min(min_val, val)
    return min_val

def printString(items):
    string = ""
    for item in items:
        string += str(item) + " "
    print(string.strip())

if __name__ == "__main__":
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5) 
    root.right.left = Node(6) 
    root.right.right = Node(7) 
    root.right.left.right =Node(8) 
    root.right.right.left = Node(10) 
    root.right.right.right = Node(9) 
    root.right.right.left.right = Node(11) 
    root.right.right.left.right.right = Node(12) 

    printVerticalOrder(root)