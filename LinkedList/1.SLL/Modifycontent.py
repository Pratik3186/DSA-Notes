class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def ModifyContent(head,old_value,new_value):
        current = head
        while current is not None:
            if current.data == old_value:
                current.data = new_value
            current = current.next
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
head = Node.ModifyContent(head,20,25)
Node.traverse(head)
