class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    @staticmethod
    def LLcycle(head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
    
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

# Create cycle
node4.next = node3

head = node1

print(Node.LLcycle(head))

