class Error(Exception):
    pass

class NodeNotFoundError(Error):
    pass
    
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
    
    def search(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node
    
    def insertHead(self, node):
        if not isinstance(node, Node):
            node = Node(node)
        if self.head is None:
            self.head = node
            self.tail = node
        elif self.head is self.tail:
            self.head = node
            node.next = self.tail
            self.tail.prev = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        return True
    
    def insertTail(self, node):
        if not isinstance(node, Node):
            node = Node(node)
        if self.tail is None:
            self.head = node
            self.tail = node
        elif self.tail is self.head:
            self.tail = node
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        return True
    
    def insertAfter(self, node, new_node):
        if not isinstance(new_node, Node):
            new_node = Node(new_node)
        if not isinstance(node, Node):
            node = self.search(node)
            if node is None:
                return False
        if node.next is None:
            return self.insertTail(new_node)
        node.next.prev = new_node
        new_node.next = node.next
        new_node.prev = node
        node.next = new_node
        return True
    
    def removeHead(self):
        if self.head is None:
            return False
        tmp = self.head.value
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return tmp
    
    def removeTail(self):
        if self.tail is None:
            return False
        tmp = self.tail.value
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return tmp
    
    def remove(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        if node is None:
            return False
        elif node is self.head:
            return self.removeHead()
        elif node is self.tail:
            return self.removeTail()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            return node.value
        
    def printList(self):
        node = self.head
        string = ''
        while node is not None:
            string += str(node.value) + ' '
            node = node.next
        print(string)
    
    def printreverse(self):
        node = self.tail
        string = ''
        while node is not None:
            string += str(node.value) + ' '
            node = node.prev
        print(string)
        
    def printHead(self):
        if self.head is not None:
            print(self.head.value)
        else:
            print(None)
    
    def printTail(self):
        if self.tail is not None:
            print(self.tail.value)
        else:
            print(None)
            
            
if __name__ == '__main__':
    dll = DoublyLinkedList()
    print(dll.removeHead())
    print(dll.removeTail())
    print(dll.remove(1))
    print(dll.insertAfter(None, Node(11)))
    print(dll.remove(11))
    print(dll.remove(3))
    dll.printList()
    dll.printHead()
    dll.printTail()
    dll.insertHead(Node(1))
    dll.insertHead(Node(2))
    dll.insertHead(Node(3))
    dll.printList()
    dll.printHead()
    dll.printTail()
    print(dll.removeHead())
    a = Node(4)
    b = Node(6)
    dll.insertTail(a)
    dll.insertTail(Node(5))
    dll.insertTail(b)
    dll.printList()
    dll.printHead()
    dll.printTail()
    dll.insertAfter(a, Node(8))
    dll.insertAfter(a, Node(9))
    dll.printList()
    dll.printHead()
    dll.printTail()
    dll.insertAfter(b, Node(10))
    print(dll.removeHead())
    print(dll.removeTail())
    print(dll.remove(9))
    dll.printList()
    dll.printHead()
    dll.printTail()
    dll.printreverse()
    dll.insertHead(5)
    dll.printList()
    dll.insertAfter(None, 111)
    dll.printList()
    dll.insertAfter(-1, 111)
    dll.printList()