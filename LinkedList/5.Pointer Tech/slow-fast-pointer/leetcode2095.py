class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def removeMiddle(head):
        if head is None:
            return None
        if head.next is None:
            return None
        prev = head
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head 
    def traverse(head):
        current = head 
        while current is not None:
            print(current.data, end='->' )
            current = current.next
        print('None')
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

head = Node.removeMiddle(head)
Node.traverse(head)



