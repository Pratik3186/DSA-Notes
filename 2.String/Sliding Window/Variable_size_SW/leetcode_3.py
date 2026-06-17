def longestsubstring(s):
    left = 0
    seen = set()
    max_length = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left = left+1
        seen.add(s[right])
        max_length=max(max_length, right -left+1)
    return max_length 

s = 'a','b','c','a','b','c','b','b'
result = longestsubstring(s)
print(result)