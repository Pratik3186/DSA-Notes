class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def countNode(head):
        count = 0
        current = head
        while current is not None:
            count += 1
            current = current.next 
        return count 
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
count = Node.countNode(head)
print(count)
Node.traverse(head)
    