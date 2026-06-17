from collections import defaultdict
class Solution:
    @staticmethod
    def fruitsbasket(fruits):
        left = 0
        freq = defaultdict(int)
        ans = 0
        for right in range(len(fruits)):
            freq[fruits[right]] += 1
            while len(freq) > 2:
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]] 
                left += 1
            ans = max(ans, right-left+1)
        return ans 
    
if __name__ == '__main__':
    fruits = [3,3,3,1,2,1,1,2,3,3,4]
    result = Solution.fruitsbasket(fruits)
    print(result)