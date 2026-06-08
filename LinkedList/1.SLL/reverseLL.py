class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def ReverseLL(head):
        prev = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    def traverse(head):
        current = head
        while current is not None:
            print(current.data, end = '->')
            current = current.next
        print('None')
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head = Node.ReverseLL(head)
Node.traverse(head)
