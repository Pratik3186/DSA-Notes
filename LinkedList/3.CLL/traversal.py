# SLL method 
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
    def traversal(head):
        if head is None:
            return
        current = head
        while current.next != head:
            print(current.data, end="->")
            current = current.next
        print(current.data, end='->')
        print('head')

# Create nodes
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

# Make it circular
head.next.next.next.next = head

# Traverse
Node.traversal(head)

# DLL method 
