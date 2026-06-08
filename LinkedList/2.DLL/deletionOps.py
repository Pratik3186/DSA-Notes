class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

    def deletehead(head):
        if head is None:
            return head 
        current = head 
        head = head.next
        if head is not None:
            head.prev = None
        return head 
    def deleteEnd(head):
        if head is None:
            return None
        current = head 
        while current.next is not None:
            current = current.next
        if current.prev is not None:
            current.prev.next = None
        return head 
    
    def deletePos(head,pos):
        if head is None:
            return head 
        current = head 
        for i in range(1,pos):
            if current is None:
                return head
            current = current.next
        if current is None:
            return head
        if current.prev is not None:
            current.prev.next = current.next
        if current.next is not None:
            current.next.prev = current.prev

        if head == current:
            head = current.next 
            if head is not None:
                head.prev = None
        del current
        return head 
    def traverse(head):
        current = head 
        while current is not None:
            print(current.data, end ='<->')
            current = current.next
        print('None')
    
head = Node(10)

head.next = Node(20)
head.next.prev = head

head.next.next = Node(30)
head.next.next.prev = head.next

head.next.next.next = Node(40)
head.next.next.next.prev = head.next.next
# head = Node.deletehead(head)
# Node.traverse(head)

# head = Node.deleteEnd(head)
# Node.traverse(head)
head = Node.deletePos(head,3)
Node.traverse(head)
