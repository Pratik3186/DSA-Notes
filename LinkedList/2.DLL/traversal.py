class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    def traversal(head):
        current = head 
        while current is not None:
            print(current.data, end = '<->')
            current = current.next
        print('None')

head = Node(10)
head.next = Node(20)
head.next.prev = head

head.next.next = Node(30)
head.next.next.prev = head.next

head.next.next.next = Node(40)
head.next.next.next.prev = head.next.next

head.next.next.next.next = Node(50)
head.next.next.next.next.prev = head.next.next.next

Node.traversal(head)