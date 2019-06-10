#Challenge: Given the head of a singly linked list, reverse it in-place.

from LinkedList import Node, LinkedList as ll

def reverseLinkedList(head, fix_head):
    if head == None or head.next == None:
        return head
    new_head = reverseLinkedList(head.next, head)
    next_node = head.next
    next_node.next = head
    if head == fix_head:
        head.next = None
    return new_head

if __name__ == '__main__':
    l = ll()
    l.insertHead(Node(1))
    l.insertHead(Node(2))
    l.insertHead(Node(3))
    l.insertHead(Node(4))
    l.insertHead(Node(5))
    l.insertHead(Node(6))
    l.insertHead(Node(7))
    l.insertHead(Node(8))
    l.insertHead(Node(9))
    l.insertHead(Node(10))
    l.printList()
    l.head = reverseLinkedList(l.head, l.head)
    l.printList()
    print("==================================")
    l = ll()
    l.head = reverseLinkedList(l.head, l.head)
    l.printList()
    print("==================================")
    l = ll()
    l.insertHead(Node(1))
    l.head = reverseLinkedList(l.head, l.head)
    l.printList()