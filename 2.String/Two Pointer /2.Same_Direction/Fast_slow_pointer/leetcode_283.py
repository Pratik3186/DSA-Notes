class Solution:
    @staticmethod
    def moveZeros(nums):
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow +=1 


if __name__ == '__main__':
    nums = [0,1,0,4,7,3,0]
    result = Solution.moveZeros(nums)
    print(result)

