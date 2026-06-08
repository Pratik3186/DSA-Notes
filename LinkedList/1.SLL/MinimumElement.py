class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def MinimumElement(head):
        if head is None:
            return None
        Minimum = head.data
        current = head
        while current is not None:
            if current.data < Minimum:
                print(current.data, end = '->')
            current = current.next
        return Minimum
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

Min = Node.MinimumElement(head)
print(Min)
