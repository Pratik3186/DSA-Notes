from collections import defaultdict , Counter
class Solution:
    @staticmethod
    def minSubarray(s:str, t:str):
        left = 0
        need = Counter(t)
        required = len(need)
        formed = 0
        window = defaultdict(int)
        min_len = float('inf')
        start = 0

        for right in range(len(s)):
            char = s[right]
            window[char] += 1
            if char in need and window[char] == need[char]:
                formed += 1
            while formed == required:
                if right - left +1 < min_len:
                    min_len = right - left +1
                    start = left 
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] <need[left_char]:
                    formed -= 1
                left +=1
        if min_len == float('inf'):
            return ''

        return s[start:start+min_len]

if __name__ == '__main__':
    s = 'ADOBECODEBANC'
    t = 'ABC'
    result = Solution.minSubarray(s,t)
    print(result) 

    

