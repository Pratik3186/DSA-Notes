class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def traverse(head):
        current = head
        while current is not None:
            print(current.data, end='->')
            current = current.next
        print('None')
    def insertStart(head,data):
        new_node = Node(data)
        new_node.next = head
        head = new_node
        return head
    def insertEnd(head,data):
        new_node = Node(data)
        if head is None:
            return None
        current = head
        while current.next is not None:
            current = current.next
        current.next = new_node
        return head 
    def insertpos(head,data,pos):
        new_node = Node(data)
        if pos == 0:
            new_node.next = head
            return new_node
        current = head
        for i in range(1,pos):
            if current is None:
                return head
        current = current.next
        if current is None:
            return head
        new_node.next = current.next
        current.next = new_node
        return head 
    
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next =  Node(40)
print('Before insertion')
Node.traverse(head)

head = Node.insertStart(head, 5)

print('after insertion')

Node.traverse(head)

head = Node.insertEnd(head, 50)

print('after insert at the end ')

Node.traverse(head)

print('insertpos')
head = Node.insertpos(head,25,3)
Node.traverse(head)
        

    