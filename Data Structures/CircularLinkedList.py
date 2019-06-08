class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
class CircularLinkedList:
    def __init__(self, node=None):
        self.length = 0
        self.tail = node
        if node is not None:
            node.next = node
            self.length += 1
    
    def __len__(self):
        return self.length
    
    def search(self, item):
        node = self.tail
        count = 1
        while node is not None and node.value != item and count <= self.length:
            node = node.next
            count += 1
        if count > self.length:
            return None
        return node
    
    def insertHead(self, item):
        if not isinstance(item, Node):
            item = Node(item)
        if self.tail is None:
            self.tail = item
            item.next = item
        else:
            item.next = self.tail.next
            self.tail.next = item
        self.length += 1
        return True
    
    def insertTail(self, item):
        node = Node(item)
        status = self.insertHead(node)
        self.tail = node 
        return status
    
    def insertAfter(self, item, new_item):
        if not isinstance(new_item, Node):
            new_item = Node(new_item)
        if not isinstance(item, Node):
            item = self.search(item)
            if item is None:
                return False
        new_item.next = item.next
        item.next = new_item
        self.length += 1
        if item == self.tail:
            self.tail = new_item
        return True
    
    def removeHead(self):
        tmp = self.tail
        if self.length == 0:
            return -1
        elif self.length == 1:
            self.tail = None
        else:
            tmp = self.tail.next
            self.tail.next = tmp.next
        self.length -= 1
        return tmp.value
    
    def removeTail(self):
        tmp = self.tail
        if self.length == 0:
            return False
        elif self.length == 1:
            self.tail = None
        else:
            node = self.tail
            while node.next != self.tail:
                node = node.next
            node.next = self.tail.next
            self.tail = node
        self.length -= 1
        return tmp.value
    
    def remove(self, item):
        prev = None
        node = self.tail
        count = 1
        if isinstance(item, Node):
            item = item.value
        while node is not None and node.value != item and count <= self.length:
            prev = node
            node = node.next
            count += 1
        if count > self.length or node is None:
            return False
        elif node == self.tail:
            return self.removeTail()
        else:
            prev.next = node.next
            if node == self.tail:
                self.tail = prev
            return item
    
    def printList(self):
        if self.tail is None:
            print("The list is empty!")
            return
        node = self.tail.next
        string = ""
        while node != self.tail:
            string += str(node.value) + " "
            node = node.next
        print(string + str(node.value))
        
    def printHead(self):
        if self.tail is not None:
            print(self.tail.next.value)
        else:
            print(None)
        
    def printTail(self):
        if self.tail is not None:
            print(self.tail.value)    
        else:
            print(None)
            
if __name__ == '__main__':            
    cll = CircularLinkedList(Node(5))
    print(len(cll))
    print(cll.removeTail())
    cll.printList()
    cll.printHead()
    cll.printTail()
    
    print(cll.insertAfter(5, 99))
    print(len(cll))
    cll.printList()
    cll.printHead()
    cll.printTail()
    
    cll = CircularLinkedList()
    print(cll.search(-1))
    print(cll.insertAfter(66, 99))
    cll.printList()
    cll.insertHead(4)
    cll.insertHead(5)
    cll.insertHead(6)
    cll.printHead()
    cll.printTail()
    cll.printList()
    
    print(cll.search(-1))
    print(cll.search(5).value)
    
    cll.insertTail(66)
    cll.printList()
    cll.printHead()
    cll.printTail()
    
    cll.insertAfter(66, 99)
    cll.insertAfter(4, 9)
    cll.insertAfter(6, 123)
    cll.printList()
    cll.printHead()
    cll.printTail()
    print(len(cll))
    
    cll.removeHead()
    cll.printList()
    cll.printHead()
    cll.printTail()
    
    cll.removeTail()
    print(cll.remove(9))
    cll.printList()
    print(cll.remove(123))
    cll.printList()
    print(cll.remove(66))
    cll.printList()
    cll.printHead()
    cll.printTail()
    
    cll = CircularLinkedList()
    print(cll.remove(0))
    print(cll.remove(None))
