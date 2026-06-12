# Sliding Window Pattern (Zero → Hero)

# 1. What is Sliding Window?

Sliding Window is a DSA technique used on **arrays** and **strings** to efficiently process **contiguous (continuous)** elements.

Instead of recalculating every subarray/substring from scratch, we maintain a window and move it across the data.

Example:

```text
Array = [2, 1, 5, 1, 3, 2]
K = 3

Windows:
[2,1,5]
[1,5,1]
[5,1,3]
[1,3,2]
```

We slide the window by:

- Removing the left element
- Adding the right element

This reduces time complexity from O(n²) to O(n) in many problems.

---

# 2. When Should You Think About Sliding Window?

If the question contains:

✅ Array

✅ String

✅ Subarray

✅ Substring

✅ Consecutive elements

✅ Contiguous elements

✅ Longest

✅ Shortest

✅ Maximum

✅ Minimum

✅ Count of valid windows

Think:

"Can Sliding Window be applied?"

---

# 3. Keywords That Indicate Sliding Window

## Fixed Window Keywords

- Maximum sum of size K
- Average of size K
- First negative number in every window
- Count distinct elements in every window

## Variable Window Keywords

- Longest substring
- Shortest substring
- Smallest subarray
- At most K distinct
- Exactly K distinct
- Without repeating characters
- Sum greater than K

---

# 4. Types of Sliding Window

## A. Fixed Size Window

Window size remains constant.

Example:

```text
Find maximum sum subarray of size K
```

Window size is given.

---

## B. Variable Size Window

Window grows and shrinks dynamically.

Example:

```text
Longest substring without repeating characters
```

Window size changes.

---

# 5. Fixed Size Sliding Window Template

```python
def fixed_window(arr, k):

    window_sum = sum(arr[:k])
    ans = window_sum

    for right in range(k, len(arr)):
        window_sum += arr[right]
        window_sum -= arr[right-k]

        ans = max(ans, window_sum)

    return ans
```

Time Complexity: O(n)

Space Complexity: O(1)

---

# 6. Variable Size Sliding Window Template

```python
left = 0

for right in range(len(arr)):

    # Expand window
    add(arr[right])

    while condition_invalid:
        remove(arr[left])
        left += 1

    update_answer()
```

Time Complexity: O(n)

Space Complexity: Depends on problem

---

# 7. How Sliding Window Works

## Expand

```python
right += 1
```

Add new element into window.

## Shrink

```python
left += 1
```

Remove elements from left side.

Window:

```text
[left ........ right]
```

---

# 8. Fixed Window Example

Problem:

Maximum sum subarray of size K.

```python
def max_sum(arr, k):

    window_sum = sum(arr[:k])
    ans = window_sum

    for right in range(k, len(arr)):
        window_sum += arr[right]
        window_sum -= arr[right-k]

        ans = max(ans, window_sum)

    return ans
```

---

# 9. Variable Window Example

Longest Substring Without Repeating Characters

```python
def longest_substring(s):

    left = 0
    seen = set()
    ans = 0

    for right in range(len(s)):

        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        ans = max(ans, right-left+1)

    return ans
```

---

# 10. Sliding Window Identification Flowchart

Question asks:

Array/String?

↓

Subarray/Substring?

↓

Contiguous elements?

↓

Yes

↓

Check:

Fixed size given?

→ Fixed Window

Otherwise

→ Variable Window

---

# 11. Major Sliding Window Patterns

## Pattern 1: Maximum / Minimum Sum

Examples:

- Maximum Sum Subarray of Size K
- Maximum Average Subarray

Template:

```python
window_sum += arr[right]
window_sum -= arr[right-k]
```

---

## Pattern 2: Longest Substring

Examples:

- Longest Substring Without Repeating Characters
- Longest Repeating Character Replacement
- Longest Substring with K Distinct Characters

Template:

```python
while invalid:
    shrink()
```

---

## Pattern 3: Smallest Window

Examples:

- Minimum Window Substring
- Minimum Size Subarray Sum

Template:

```python
while valid:
    update_answer()
    shrink()
```

---

## Pattern 4: Count Valid Windows

Examples:

- Count Nice Subarrays
- Binary Subarrays With Sum

Template:

```python
count += right-left+1
```

---

## Pattern 5: At Most K Distinct

Examples:

- Fruits Into Baskets
- Longest Substring With K Distinct

Template:

```python
freq[s[right]] += 1

while len(freq) > k:
    shrink()
```

---

## Pattern 6: Exactly K Distinct

Formula:

```python
Exactly(K)
= AtMost(K) - AtMost(K-1)
```

---

## Pattern 7: Frequency Map Window

Used when character counts matter.

Example:

- Minimum Window Substring

Template:

```python
freq = {}

freq[ch] += 1
freq[ch] -= 1
```

---

# 12. Common Data Structures Used

## Set

Used for uniqueness.

```python
seen = set()
```

Example:

Longest Substring Without Repeating Characters

---

## Dictionary / HashMap

Used for frequency counting.

```python
freq = {}
```

Example:

Minimum Window Substring

---

## Queue / Deque

Used for Sliding Window Maximum.

```python
from collections import deque
```

---

# 13. Important LeetCode Problems

## Beginner

LC 643 - Maximum Average Subarray I

LC 1456 - Maximum Number of Vowels

---

## Easy-Medium

LC 3 - Longest Substring Without Repeating Characters

LC 209 - Minimum Size Subarray Sum

---

## Medium

LC 1004 - Max Consecutive Ones III

LC 424 - Longest Repeating Character Replacement

LC 904 - Fruit Into Baskets

---

## Hard

LC 76 - Minimum Window Substring

LC 239 - Sliding Window Maximum

---

# 14. Complexity Analysis

Typical Sliding Window:

```python
left = 0

for right in range(n):
```

Each element enters once.

Each element leaves once.

Therefore:

Time Complexity:

```text
O(n)
```

Space Complexity:

```text
O(1) to O(n)
```

---

# 15. Common Mistakes

❌ Forgetting to shrink window

❌ Using if instead of while

❌ Updating answer before validating window

❌ Wrong window size formula

Correct:

```python
right-left+1
```

---

# 16. Ultimate Sliding Window Template

```python
def sliding_window(arr):

    left = 0
    answer = 0

    for right in range(len(arr)):

        # Expand
        add(arr[right])

        while window_invalid:

            # Shrink
            remove(arr[left])
            left += 1

        # Update answer
        answer = max(answer, right-left+1)

    return answer
```

---

# 17. Interview Cheat Sheet

## Fixed Window

```python
window = first_window

for right in range(k, n):
    add_new_element
    remove_old_element
```

## Variable Window

```python
for right in range(n):

    expand

    while invalid:
        shrink

    update_answer
```

## Exactly K Distinct

```python
AtMost(K) - AtMost(K-1)
```

## Window Size

```python
right-left+1
```

---

# 18. Mastery Roadmap

Day 1:
- Fixed Window

Day 2:
- Maximum Sum Problems

Day 3:
- Longest Substring Problems

Day 4:
- K Distinct Problems

Day 5:
- Minimum Window Problems

Day 6:
- Sliding Window Maximum

Day 7:
- Mixed Practice

After mastering these patterns, you can solve most Sliding Window interview questions.