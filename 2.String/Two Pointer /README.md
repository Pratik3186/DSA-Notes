# Two Pointers Pattern — Complete Interview Guide

## What is the Two Pointer Technique?

Instead of using a single index:

```python
i
```

we use **two indices (pointers)**:

```python
left
right
```

to solve problems efficiently.

Example:

```text
arr = [1, 2, 3, 4, 5]

L               R
1   2   3   4   5
```

Move pointers based on conditions:

```text
L →
← R
```

until the required condition is met.

### Why Use Two Pointers?

- Reduces nested loops
- Optimizes brute-force solutions
- Often reduces complexity from O(n²) → O(n)
- Commonly asked in coding interviews

---

# How to Identify Two Pointer Problems

Look for keywords like:

- Pair
- Sorted Array
- Palindrome
- Reverse
- Remove Duplicates
- Container
- Triplets
- Four Sum
- Merge

### Interview Trigger

Whenever you see:

```text
Find two numbers...
Find pair...
Sorted array...
Check palindrome...
```

Think:

```text
🔥 Two Pointers
```

---

# Two Pointer Pattern Family

```text
Arrays / Strings
      │
      └── Two Pointers
             │
             ├── Opposite Direction
             ├── Same Direction (Fast-Slow)
             ├── Sliding Window
             ├── Merge Two Arrays
             ├── K-Sum Family
             ├── Linked List Fast-Slow
             └── Partition / Dutch National Flag
```

---

# Pattern 1: Opposite Direction Pointers

## Visualization

```text
L               R
1   2   3   4   5
```

Move inward:

```text
L →
← R
```

## Identification

Keywords:

- Sorted Array
- Pair Sum
- Palindrome
- Container
- Two Ends
- Triplets

## Template

```python
left = 0
right = len(arr) - 1

while left < right:

    if condition:
        return answer

    elif need_larger_value:
        left += 1

    else:
        right -= 1
```

## Famous Problems

| LC | Problem |
|----|----------|
| 167 | Two Sum II |
| 125 | Valid Palindrome |
| 11 | Container With Most Water |
| 977 | Squares of a Sorted Array |
| 15 | 3Sum |
| 18 | 4Sum |
| 881 | Boats to Save People |

---

# Pattern 2: Same Direction (Fast-Slow Pointer)

## Visualization

```text
slow
 ↓
1 1 2 2 3

fast
      ↓
```

Both pointers move forward.

## Identification

Keywords:

- Remove
- Duplicates
- Compress
- Move Zeroes
- Modify In-Place

## Template

```python
slow = 0

for fast in range(len(nums)):

    if valid(nums[fast]):
        nums[slow] = nums[fast]
        slow += 1
```

## Famous Problems

| LC | Problem |
|----|----------|
| 26 | Remove Duplicates from Sorted Array |
| 27 | Remove Element |
| 283 | Move Zeroes |
| 75 | Sort Colors |
| 443 | String Compression |
| 1089 | Duplicate Zeros |
| 80 | Remove Duplicates from Sorted Array II |

---

# Pattern 3: Sliding Window

Sliding Window is actually a specialized Two Pointer pattern.

## Visualization

```text
L       R
[a b c d]
```

Both pointers move forward.

## Already Covered

| LC | Problem |
|----|----------|
| 3 | Longest Substring Without Repeating Characters |
| 424 | Longest Repeating Character Replacement |
| 904 | Fruit Into Baskets |
| 209 | Minimum Size Subarray Sum |
| 76 | Minimum Window Substring |
| 1358 | Number of Substrings Containing All Three Characters |
| 992 | Subarrays With K Different Integers |

---

# Pattern 4: Merge Two Arrays / Two Streams

## Visualization

```text
A → → →
B → → →
```

Compare elements from both arrays and move pointers accordingly.

## Identification

Keywords:

- Merge
- Intersection
- Union
- Two Sorted Arrays
- Compare Streams

## Template

```python
i = 0
j = 0

while i < len(A) and j < len(B):

    if A[i] == B[j]:
        i += 1
        j += 1

    elif A[i] < B[j]:
        i += 1

    else:
        j += 1
```

## Famous Problems

| LC | Problem |
|----|----------|
| 88 | Merge Sorted Array |
| 350 | Intersection of Two Arrays II |
| 349 | Intersection of Two Arrays |
| 1768 | Merge Strings Alternately |
| 165 | Compare Version Numbers |
| 243 | Shortest Word Distance |
| 599 | Minimum Index Sum of Two Lists |

---

# Pattern 5: K-Sum Family

One of the most important interview patterns.

## Identification

Keywords:

- Triplet
- Three Numbers
- Four Numbers
- Target Sum
- Combination Sum

## Core Idea

```text
Fix one element
Apply Two Pointers on remaining elements
```

## Example (3Sum)

```python
for i in range(len(nums)):

    left = i + 1
    right = len(nums) - 1

    while left < right:

        total = nums[i] + nums[left] + nums[right]

        if total == target:
            pass

        elif total < target:
            left += 1

        else:
            right -= 1
```

## Famous Problems

| LC | Problem |
|----|----------|
| 15 | 3Sum |
| 16 | 3Sum Closest |
| 18 | 4Sum |
| 259 | 3Sum Smaller |
| 923 | 3Sum With Multiplicity |
| 167 | Two Sum II |
| 1099 | Two Sum Less Than K |

---

# Pattern 6: Linked List Fast-Slow Pointer

Two Pointer technique applied on Linked Lists.

## Visualization

```text
slow → 1 step

fast → 2 steps
```

## Identification

Keywords:

- Middle Node
- Cycle Detection
- Loop
- Nth Node
- Palindrome Linked List

## Template

```python
slow = head
fast = head

while fast and fast.next:

    slow = slow.next
    fast = fast.next.next
```

## Famous Problems

| LC | Problem |
|----|----------|
| 876 | Middle of the Linked List |
| 141 | Linked List Cycle |
| 142 | Linked List Cycle II |
| 234 | Palindrome Linked List |
| 19 | Remove Nth Node From End |
| 143 | Reorder List |
| 160 | Intersection of Two Linked Lists |

---

# Pattern 7: Partition / Dutch National Flag

Used for rearranging elements into groups.

## Identification

Keywords:

- Sort 0 1 2
- Partition
- Colors
- Pivot
- Rearrange

## Visualization

```text
[0s | 1s | Unknown | 2s]
```

Three pointers:

```python
low
mid
high
```

## Template

```python
low = 0
mid = 0
high = len(nums) - 1

while mid <= high:

    if nums[mid] == 0:
        nums[low], nums[mid] = nums[mid], nums[low]
        low += 1
        mid += 1

    elif nums[mid] == 1:
        mid += 1

    else:
        nums[mid], nums[high] = nums[high], nums[mid]
        high -= 1
```

## Famous Problems

| LC | Problem |
|----|----------|
| 75 | Sort Colors |
| 2161 | Partition Array According to Given Pivot |
| 280 | Wiggle Sort |
| 2149 | Rearrange Array Elements by Sign |
| 283 | Move Zeroes |
| 905 | Sort Array By Parity |
| 922 | Sort Array By Parity II |

---

# Recommended Learning Order

## Phase 1 (Must Master)

| LC | Problem |
|----|----------|
| 125 | Valid Palindrome |
| 26 | Remove Duplicates from Sorted Array |
| 27 | Remove Element |
| 283 | Move Zeroes |
| 167 | Two Sum II |
| 11 | Container With Most Water |

## Phase 2

| LC | Problem |
|----|----------|
| 88 | Merge Sorted Array |
| 350 | Intersection of Two Arrays II |
| 75 | Sort Colors |
| 977 | Squares of a Sorted Array |
| 443 | String Compression |

## Phase 3

| LC | Problem |
|----|----------|
| 15 | 3Sum |
| 16 | 3Sum Closest |
| 18 | 4Sum |

## Phase 4 (Linked List Two Pointer)

| LC | Problem |
|----|----------|
| 876 | Middle of the Linked List |
| 141 | Linked List Cycle |
| 142 | Linked List Cycle II |
| 19 | Remove Nth Node From End |
| 234 | Palindrome Linked List |
| 143 | Reorder List |

---

# The 6 Problems That Teach Almost Everything

| Order | LC | Problem | Pattern |
|--------|----|----------|----------|
| 1 | 125 | Valid Palindrome | Opposite Direction |
| 2 | 26 | Remove Duplicates | Fast-Slow |
| 3 | 283 | Move Zeroes | Fast-Slow |
| 4 | 167 | Two Sum II | Opposite Direction |
| 5 | 11 | Container With Most Water | Opposite Direction |
| 6 | 15 | 3Sum | K-Sum |

---

# Quick Revision Cheat Sheet

```text
PAIR + SORTED ARRAY
    → Opposite Direction

REMOVE / DUPLICATES
    → Fast-Slow

SUBARRAY / SUBSTRING
    → Sliding Window

MERGE / INTERSECTION
    → Two Streams

TRIPLET / FOUR SUM
    → K-Sum

MIDDLE / CYCLE
    → Fast-Slow Linked List

SORT 0 1 2 / PIVOT
    → Dutch National Flag
```

---

# DSA Roadmap Progress

```text
Strings
   │
   └── Sliding Window ✅
           │
           ├── Fixed Window
           ├── Variable Window
           ├── Minimum Window
           ├── Counting Window
           └── Exactly K Window

Arrays / Strings
   │
   └── Two Pointers ✅
           │
           ├── Opposite Direction
           ├── Fast-Slow
           ├── Sliding Window
           ├── Merge Arrays
           ├── K-Sum
           ├── Linked List Fast-Slow
           └── Dutch National Flag

Next Topic →
Stack & Monotonic Stack
```

## Goal

Solve these 6 problems first:

1. LC 125 – Valid Palindrome
2. LC 26 – Remove Duplicates from Sorted Array
3. LC 283 – Move Zeroes
4. LC 167 – Two Sum II
5. LC 11 – Container With Most Water
6. LC 15 – 3Sum

After mastering these, you'll recognize most Two Pointer interview questions within seconds.