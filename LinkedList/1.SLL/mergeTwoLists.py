class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    def mergeTwoLists(list1,list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            list1.next = Node.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = Node.mergeTwoLists(list1, list2.next)
            return list2
    
    def traverse(head):
        current = head
        while current is not None:
            print(current.val, end = '->')
            current = current.next
        print('None')

list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(3)
list2= Node(2)
list2.next = Node(3)
list2.next.next = Node(4)

head = Node.mergeTwoLists(list1,list2)
Node.traverse(head )