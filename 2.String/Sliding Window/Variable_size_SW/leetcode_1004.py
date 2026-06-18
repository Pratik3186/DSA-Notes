class Solution:
    @staticmethod
    def longestOnes(nums,k):
        left = 0
        zero_count = 0
        ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            while zero_count >k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            ans = max(ans,right-left+1)
        return ans 
    
if __name__ == '__main__':
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    result = Solution.longestOnes(nums,k)
    print(result)