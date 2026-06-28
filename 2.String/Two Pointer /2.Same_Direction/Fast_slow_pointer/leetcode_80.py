class Solution:
    @staticmethod
    def removeDuplicate(nums):
        if len(nums)<=2:
            return len(nums)
        slow = 2
        for fast in range(2,len(nums)):
            if nums[fast] != nums[slow-2]:
                nums[slow] = nums[fast]
                slow+=1
        return slow
    
if __name__ == '__main__':
    nums = [1,1,1,1,2,2,2,3,3,3,4,4,4,4,4,5,5]
    result = Solution.removeDuplicate(nums)
    print(nums[:result])