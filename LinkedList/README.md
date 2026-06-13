# Linked List Mastery Notes (A to Z)

# 1. What is a Linked List?

A Linked List is a linear data structure where elements are stored in nodes.

Each node contains:

* Data
* Pointer to next node

Example:

10 -> 20 -> 30 -> 40 -> None

Node Structure:

```python
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
```

---

# 2. Traversal

Algorithm:

1. Start from head.
2. Visit node.
3. Move to next node.
4. Stop at None.

```python
def traverse(head):

    current = head

    while current is not None:
        print(current.data,end="->")
        current = current.next

    print("None")
```

Time Complexity: O(n)

---

# 3. Insertion Operations

## Insert At Beginning

```python
new_node.next = head
head = new_node
```

Time: O(1)

---

## Insert At End

```python
current = head

while current.next is not None:
    current = current.next

current.next = new_node
```

Time: O(n)

---

## Insert At Position

Steps:

1. Reach position-1
2. Connect new node

```python
new_node.next = current.next
current.next = new_node
```

Time: O(n)

---

# 4. Deletion Operations

## Delete Head

```python
head = head.next
```

Time: O(1)

---

## Delete Last Node

Reach second last node.

```python
current.next = None
```

Time: O(n)

---

## Delete At Position

```python
current.next = current.next.next
```

Time: O(n)

---

# 5. Searching

```python
current = head

while current:

    if current.data == key:
        return True

    current = current.next

return False
```

Time: O(n)

---

# 6. Modify Content

```python
while current:

    if current.data == old_value:
        current.data = new_value

    current = current.next
```

---

# 7. Count Nodes / Length

```python
count = 0

while current:

    count += 1
    current = current.next
```

Time: O(n)

---

# 8. Maximum Element

```python
maximum = head.data

while current:

    maximum = max(maximum,current.data)

    current = current.next
```

Time: O(n)

---

# 9. Minimum Element

```python
minimum = head.data

while current:

    minimum = min(minimum,current.data)

    current = current.next
```

Time: O(n)

---

# 10. Find Middle Node

Pattern: Slow and Fast Pointer

```python
slow = head
fast = head

while fast and fast.next:

    slow = slow.next
    fast = fast.next.next

return slow
```

Time: O(n)

Space: O(1)

Important Problem:
LeetCode 876

---

# 11. Reverse Linked List

Pattern:

```python
prev = None
current = head

while current:

    next_node = current.next

    current.next = prev

    prev = current

    current = next_node

return prev
```

Remember:

Save
Reverse
Move Prev
Move Current

LeetCode 206

---

# 12. Merge Two Sorted Linked Lists

Recursive Pattern:

```python
if list1 is None:
    return list2

if list2 is None:
    return list1

if list1.val <= list2.val:

    list1.next = merge(list1.next,list2)

    return list1

else:

    list2.next = merge(list1,list2.next)

    return list2
```

LeetCode 21

---

# 13. Remove Nth Node From End

Pattern:

Fast Pointer First

```python
slow = dummy
fast = dummy

move fast n+1 steps

move both until fast becomes None

slow.next = slow.next.next
```

LeetCode 19

---

# 14. Reorder Linked List

Pattern:

Find Middle
+
Reverse Second Half
+
Merge

LeetCode 143

---

# 15. Detect Cycle

Floyd Cycle Detection

```python
slow = head
fast = head

while fast and fast.next:

    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        return True
```

LeetCode 141

---

# 16. Detect Cycle Using HashSet

```python
seen = set()

while current:

    if current in seen:
        return True

    seen.add(current)

    current = current.next
```

Time: O(n)

Space: O(n)

---

# 17. Circular Linked List

Last node points back to head.

```python
last.next = head
```

---

# Circular LL Traversal

```python
current = head

while True:

    print(current.data)

    current = current.next

    if current == head:
        break
```

---

# Circular LL Insert At Beginning

O(n)

1. Find last node.
2. last.next = new_node
3. new_node.next = head
4. head = new_node

---

# Circular LL Insert At End

```python
last.next = new_node
new_node.next = head
```

---

# Circular LL Delete Head

Optimized O(1)

```python
head.data = head.next.data
head.next = head.next.next
```

---

# Circular LL Delete Kth Node

```python
current.next = current.next.next
```

after reaching position-1.

---

# Doubly Linked List

Node:

```python
class Node:

    def __init__(self,data):

        self.prev = None
        self.data = data
        self.next = None
```

---

# DLL Insertion

## Beginning

```python
new_node.next = head

head.prev = new_node

head = new_node
```

---

# DLL Deletion

Core Idea:

```python
current.prev.next = current.next

current.next.prev = current.prev
```

---

# Most Important Patterns

## Pattern 1

Traversal

```python
current = current.next
```

---

## Pattern 2

Insertion

```python
new_node.next = current.next
current.next = new_node
```

---

## Pattern 3

Deletion

```python
current.next = current.next.next
```

---

## Pattern 4

Reverse

```python
next_node = current.next
current.next = prev
prev = current
current = next_node
```

---

## Pattern 5

Slow Fast Pointer

```python
slow = slow.next
fast = fast.next.next
```

Used In:

* Middle Node
* Cycle Detection
* Palindrome LL
* Reorder LL

---

# Common Mistakes You Made (Very Common)

1. Writing

```python
current = current.data
```

instead of

```python
current = current.next
```

2. Forgetting:

```python
return head
```

3. Using

```python
while current is not head
```

for normal LL.

Should be:

```python
while current is not None
```

4. Forgetting:

```python
current = current.next
```

inside traversal.

Causes infinite loop.

5. Writing:

```python
head = Node.countNodes(head)
```

Count returns integer, not linked list.

6. Forgetting:

```python
prev = None
```

during reverse.

7. Using:

```python
current.data
```

when node contains:

```python
current.val
```

in LeetCode.

---

# Top Interview Questions

Easy

1. Reverse Linked List (206)
2. Middle of Linked List (876)
3. Linked List Cycle (141)
4. Merge Two Sorted Lists (21)
5. Remove Linked List Elements (203)

Medium

1. Remove Nth Node From End (19)
2. Reorder List (143)
3. Reverse Linked List II (92)
4. Add Two Numbers (2)
5. Odd Even Linked List (328)

Hard

1. Reverse Nodes in K Group (25)
2. Merge K Sorted Lists (23)
3. Copy List With Random Pointer (138)

---

# Golden Rule

Whenever stuck in Linked List:

Ask:

1. Do I need traversal?
2. Do I need previous node?
3. Is this insertion?
4. Is this deletion?
5. Is this reverse?
6. Can Slow/Fast Pointer help?

90% of linked list interview questions are combinations of these patterns.
