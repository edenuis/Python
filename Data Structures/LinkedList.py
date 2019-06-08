class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
    
    def search(self, item):
        node = self.head
        while node is not None and node.value != item:
            node = node.next
        return node
    
    def insertHead(self, item):
        if not isinstance(item, Node):
            item = Node(item)
        if self.head is None:
            self.head = item
            self.tail = item
        else:
            item.next = self.head
            self.head = item
        return True
    
    def insertTail(self, item):
        if not isinstance(item, Node):
            item = Node(item)
        if self.tail is None:
            self.head = item
            self.tail = item
        else:
            self.tail.next = item
            self.tail = item
        return True
    
    def insertAfter(self, item, new_item):
        if not isinstance(new_item, Node):
            new_item = Node(new_item)
        if not isinstance(item, Node):
            item = self.search(item)
            if item is None:
                return False
        if item.next is None:
            return self.insertTail(new_item)
        new_item.next = item.next
        item.next = new_item
        return True
    
    def removeHead(self):
        tmp = self.head
        if self.head is None:
            return False
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return tmp.value
    
    def removeTail(self):
        tmp = self.tail
        if self.tail is None:
            return False
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            node = self.head
            while node.next != self.tail:
                node = node.next
            self.tail = node
            self.tail.next = None
        return tmp.value
    
    def remove(self, item):
        prev = None
        node = self.head
        if isinstance(item, Node):
            item = item.value
        while node is not None and node.value != item:
            prev = node
            node = node.next
        if node is None:
            return False
        elif  prev is None:
            return self.removeHead()
        else:
            prev.next = node.next
            if node.next is None:
                self.tail = prev
            return item
        
    def printList(self):
        node = self.head
        string = ""
        while node is not None:
            string += str(node.value) + " "
            node = node.next
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
    ll = LinkedList()
    print(ll.removeHead())
    ll.insertHead(Node(4))
    ll.insertHead(6)
    ll.printList()
    
    ll.insertTail(7)
    ll.printList()
    ll.printTail()
    ll.printHead()
    
    print(ll.insertAfter(-1, 5))
    print(ll.insertAfter(4, 88))
    ll.printList()
    ll.printTail()
    ll.printHead()
    print(ll.insertAfter(7, 98))
    ll.printList()
    ll.printTail()
    ll.printHead()
    
    print(ll.removeTail())
    ll.printList()
    ll.printHead()
    ll.printTail()
    
    print(ll.remove(6))
    ll.printList()
    ll.printHead()
    ll.printTail()
    
    print(ll.removeTail())
    ll.printList()
    ll.printHead()
    ll.printTail()
    
    print(ll.remove(88))
    ll.printList()
    ll.printHead()
    ll.printTail()
    
    print(ll.removeTail())
    ll.printList()
    ll.printHead()
    ll.printTail()
    
    ll.insertHead(Node(4))
    ll.insertHead(6)
    ll.printList()
    
    ll.insertTail(7)
    ll.printList()
    ll.printTail()
    ll.printHead()
    
    print(ll.insertAfter(-1, 5))
    print(ll.insertAfter(4, 88))
    ll.printList()
    ll.printTail()
    ll.printHead()