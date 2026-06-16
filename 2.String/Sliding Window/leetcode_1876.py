from collections import defaultdict
class Solution:
    @staticmethod
    def countgoodSubstring(s):
        k = 3
        if len(s) < 3:
            return 0
        freq = defaultdict(int)
        for ch in s[:k]:
            freq[ch] += 1
        
        count = 1 if len(freq) == 3 else 0

        

        for right in range(k,len(s)):
            freq[s[right]] += 1
            freq[s[right-k]] -=1

            if freq[s[right-k]] == 0:
                del freq[s[right-k]]
            if len(freq) == 3:
                count+=1  

        return count      

if __name__ == '__main__':
    s = 'xyzzaz'
    result = Solution.countgoodSubstring(s)
    print(result)