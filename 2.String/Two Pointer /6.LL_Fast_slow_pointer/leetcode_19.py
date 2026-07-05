class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def removeNode(head,n):
        dummy = Node(0)
        dummy.next = head

        slow = dummy 
        fast = dummy

        for i in range(n+1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next 
        return dummy.next
    
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

new_Ll = Node.removeNode(head,2)

curr = head
while curr:
    print(curr.data, end='->')
    curr = curr.next
print(None)