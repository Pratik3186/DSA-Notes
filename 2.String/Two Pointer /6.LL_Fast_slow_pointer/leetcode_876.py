class Node:
    # @staticmethod
    def __init__(self,data):
        self.data= data
        self.next = None
    def middleofLL(head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

Middle = Node.middleofLL(head)
print(Middle.data)
