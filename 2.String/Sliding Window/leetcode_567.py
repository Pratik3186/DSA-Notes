from collections import Counter
class Solution:
    @staticmethod
    def permutationstring(s1,s2):
        k = len(s1)
        if k < len(s2):
            return False
        p_count = Counter(s1)
        window_count = Counter(s2[:k])
        if window_count == p_count:
            return True
        for right in range(k,len(s2)):
            window_count[s2[right]] += 1
            window_count[s2[right-k]] -=1

            if window_count[s2[right]] == 0:
                del window_count[s2[right-k]]
            if window_count == p_count:
                return True     
        return False
    
    
if __name__ == '__main__':
    s1 = 'ab'
    s2 = 'eidbaooo'
    result = Solution.permutationstring(s1,s2)
    print(result)
