class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def insertatStart(head,data):
        new_node = Node(data)
        current = head
        if head is None:
            new_node.next = new_node
            return new_node
        while current.next is not head: 
            current = current.next 
        current.next = new_node
        new_node.next = head 
        head = new_node
        return head
    def insertatEnd(head,data):
        new_node = Node(data)
        if head is None:
            new_node.next = head
            return new_node
        new_node.next = head.next
        head.next = new_node
        head.data, new_node.data = new_node.data, head.data
        return new_node
    
    def insertPos(head,data,pos):
        if head is None:
            if pos != 1:
                print('Invalid')
                return head 
            new_node = Node(data)
            head = new_node
            head.next = head
            return head 
        new_node = Node(data)
        current = head.next
        if pos ==1:
            new_node.next = current
            head.next = new_node
            return head
        for i in range(1,pos-1):
            current = current.next
            if current == head.next:
                print('Invalid position')
                return head
        new_node.next = current.next
        current.next= new_node

        if current == head:
            head = new_node
        return head 
    



    def traverse(head):
        if head is None:
            return head 
        current = head
        while current.next != head:
            print(current.data, end="->")
            current = current.next
        print(current.data, end='->')
        print('head')


    
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

head.next.next.next.next.next = head

head = Node.insertatStart(head,5)
Node.traverse(head)

head = Node.insertatEnd(head,6)
Node.traverse(head)

head = Node.insertPos(head, 7,2)
Node.traverse(head)

    
