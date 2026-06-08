class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

    def deteactCycle(head):
        seen = set()
        current = head
        while current:
            if current in seen:
                return True
            seen.add(current)
            current = current.next
        return False

# Create nodes
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

# Make it circular
head.next.next.next.next = head

# Traverse
print(Node.deteactCycle(head))