class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def palindromeLL(head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        current = slow
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        first = head
        second = prev
        while second:
            if first.data != second.data:
                return False
            first = first.next
            second = second.next
        return True
    
head = Node(10)
head.next = Node(20)
head.next.next = Node(20)
head.next.next.next = Node(10)

print(Node.palindromeLL(head))