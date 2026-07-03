class Solution:
    @staticmethod
    def TwoSum(nums,target):
        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement],i]
            seen[nums[i]] = i

if __name__ == '__main__':
    nums = [2,7,11,13]
    target = 9
    result = Solution.TwoSum(nums,target)
    print(result)
