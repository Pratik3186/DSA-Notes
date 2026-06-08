class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def MiddleLL(head):
        slow = head 
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next 
            fast = fast.next.next
        return slow 
    

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

Middle = Node.MiddleLL(head)
print(Middle.data)