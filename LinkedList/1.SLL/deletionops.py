class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def deleteStart(head):
        if head is None:
            return None
        cuurent = head
        head = head.next
        current = None
        return head 
    def deleteEnd(head):
        if head is None:
            return None
        if head.next is None:
            return head
        current = head
        while current.next.next is not None:
            current = current.next
        current.next = None
        return head
    def deletePos(head,pos):
        current = head
        if pos == 1:
            head = current.next 
            return head 
        prev = None
        for i in range(1,pos):
            prev = current
            current=current.next
        prev.next = current.next
        # current=None
        return head 
    def traverse(head):
        current = head
        while current is not None:
            print(current.data, end='->')
            current = current.next
        print('None')
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head = Node.deleteStart(head)
Node.traverse(head)
head = Node.deleteEnd(head)
Node.traverse(head)
head = Node.deletePos(head,3)
Node.traverse(head)