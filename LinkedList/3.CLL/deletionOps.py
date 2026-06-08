class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def deletionhead(head):
        if head is None:
            return None
        if head.next == head:
            return None
        head.data = head.next.data
        head.next = head.next.next

        return head 
    
    def nthNode(head,pos):
        if head is None:
            return None
        if pos==1:
            return Node.deletionhead(head)
        current = head
        for i in range(pos-2):
            if current.next == head:
                return head 
            current = current.next

        if current.next == head:
            return head 

        current.next = current.next.next
        return head 
    def deleteLast(head):
        if head is None:
            return None
        if head.next == head:
            return None
        current = head
        while current.next.next != head:
            current = current.next
        current.next = head
        return head
        
    
    def traverse(head):
        if head is None:
            return None
        
        current = head
        while current.next != head:
            print(current.data, end='->')
            current = current.next
        print(current.data, end='->')
        print('Head')

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head

head = Node.deletionhead(head)
Node.traverse(head)
head = Node.nthNode(head,2)
Node.traverse(head)

