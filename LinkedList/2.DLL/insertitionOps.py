class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    def InsertStart(head,new_node):
        new_node = Node(new_node)
        new_node.next = head
        if head is not None:
            head.prev = new_node
        return new_node
    
    def InsertEnd(head,new_node):
        new_node = Node(new_node)
        if head is None:
            head = new_node
        else:
            current = head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current
        return head
    def InsertPos(head, new_node,pos):
        new_node =  Node(new_node)
        if pos == 1:
            new_node.next = head
            if head is not None:
                head.prev = new_node
            head = new_node
            return head
        current = head  
        for i in range(1,pos-1):
            if current is None:
                break
            current = current.next
        if current is None:
            return head
        new_node.prev = current
        new_node.next = current.next
        current.next = new_node
        if new_node.next is not None:
            new_node.next.prev = new_node
        return head
    
    def traverse(head):
        current = head
        while current is not None:
            print(current.data, end='<->')
            current = current.next
        print('None')

head = Node(10)
head.next = Node(20)
head.next.prev = head
head.next.next = Node(30)
head.next.next.prev = head.next
head.next.next.next = Node(40)
head.next.next.next.prev = head.next.next
head.next.next.next.next = Node(50)
head.next.next.next.next.prev = head.next.next



head = Node.InsertStart(head,5)
Node.traverse(head)
head = Node.InsertEnd(head,60)
Node.traverse(head)
head = Node.InsertPos(head,25,3)
Node.traverse(head)



    
        