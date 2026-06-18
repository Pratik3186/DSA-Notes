from collections import defaultdict
class Solution:
    @staticmethod
    def subarraywithkDistinct(nums,k):
        def atmost(k):
            left = 0
            count = 0
            freq = defaultdict(int)
            for right in range(len(nums)):
                freq[nums[right]] += 1
                while len(freq) > k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1
                count += right -left +1
            return count
        return atmost(k) - atmost(k-1)  
    
if __name__ == '__main__':
    nums = [1,2,1,2,3]
    k = 2
    result = Solution.subarraywithkDistinct(nums,k)
    print(result)