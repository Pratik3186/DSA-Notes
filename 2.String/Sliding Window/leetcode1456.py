def maxVowels(s,k):
    vowel = {'a','e','i','o','u'}
    count = 0
    for ch in s[:k]:
        if ch in vowel:
            count+=1
    ans = count

    for right in range(k,len(s)):
        if s[right-k] in vowel:
            count-=1
        if s[right] in vowel:
            count+=1
        ans = max(ans,count)
    return ans

s = 'abciiidef'
k = 3
result = maxVowels(s,k)
print(result)