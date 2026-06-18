class Solution:
    @staticmethod
    def minSubArray(target,nums):
        left = 0
        window_sum = 0
        ans = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]
            while window_sum >= target:
                ans = min(ans, right-left+1)
                window_sum -= nums[left]
                left += 1
        return 0 if ans == float('inf') else ans 
    

if __name__ == '__main__':
    nums = [2,3,1,2,4,3]
    target = 7
    result = Solution.minSubArray(target,nums)
    print(result)
