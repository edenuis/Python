#Challenge: Finding middle element of linked list

#Idea: Create two pointers. One moves one node/iteration and the other moves
#      two nodes/iteration. When the pointer that moves at two nodes/iteration
#      reaches the end of linked list, the pointer that moves at one node/iteration
#      will be at the center of the linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def addNext(self, node):
        if isinstance(node, Node):
            self.next = node
        else:
            node = Node(node)
            self.next = node
    
def findCenter(head):
    one_ptr = head
    two_ptr = head
    while two_ptr is not None and two_ptr.next is not None:
        one_ptr = one_ptr.next
        two_ptr = two_ptr.next.next
    return one_ptr.value

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node1.addNext(node2)
    node2.addNext(node3)
    node3.addNext(node4)
    node4.addNext(node5)
    
    print(findCenter(node1))