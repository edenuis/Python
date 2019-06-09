#Challenge: A unival tree (which stands for "universal value") is a tree where 
#           all nodes under it have the same value. Given the root to a binary 
#           tree, count the number of unival subtrees.

#Idea: Recursively count the number of unival subtrees of root.left and root.right
#      Track: Total count at each 'root' and a True/False value that indicates
#             if the current subtree is unival or not unival.

def countUnivalSubtrees(root):
    if root.right is None and root.left is None:
        return 1, True
    left, is_left_unival = countUnivalSubtrees(root.left)
    right, is_right_unival = countUnivalSubtrees(root.right)
    
    if root.value != root.left.value or root.value != root.right.value:
        return left + right, False
    else:
        if is_left_unival and is_right_unival:
            return 1 + left + right, True
        return left + right, False
    
