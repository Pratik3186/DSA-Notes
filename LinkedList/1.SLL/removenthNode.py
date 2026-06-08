class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def removenthNode(head,n):
        dummy = Node(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        for _ in range(n+1):
            fast = fast.next
        while fast is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
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

remove = Node.removenthNode(head,3)
Node.traverse(head)