class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def MaximumElement(head):
        if head is None:
            return None
        maximum = head.data
        current = head
        while current is not None:
            if current.data > maximum:
                maximum = current.data
            current = current.next
        return maximum
    
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

max = Node.MaximumElement(head)
print(max)
