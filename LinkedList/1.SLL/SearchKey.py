class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def searchkey(head,value):
        current = head
        while current.next is not None:
            if current.data == value:
                return True
            current = current.next
        return False
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print(Node.searchkey(head, 20))