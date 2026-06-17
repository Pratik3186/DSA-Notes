from collections import Counter
class Solution:
    @staticmethod
    def findanagram(s,p):
        k = len(p)
        p_count = Counter(p)
        window_count = Counter(s[:k])
        result = []

        if window_count == p_count:
            result.append(0)
        for right in range(k,len(s)):
            window_count[s[right]]+=1
            window_count[s[right-k]] -= 1

            if window_count[s[right-k]] == 0:
                del window_count[s[right-k]]
            if window_count == p_count:
                result.append(right-k+1)

        return result
    
if __name__ == "__main__":
    s = 'cbaebabacd'
    p = 'abc'
    result = Solution.findanagram(s,p)
    print(result)
