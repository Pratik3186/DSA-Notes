#Remove duplicate element from sorted array  (fast&slow pointer)
class Solution:
    @staticmethod
    def removeduplicate(nums):
        slow = 0

        for fast in range(1,len(nums)):
              if nums[fast] != nums[slow]:
                   slow+=1
                   nums[slow] = nums[fast]
        return slow + 1 
    
if __name__ == '__main__':
     nums = [0,0,0,1,1,1,2,2,3,3,4,4,4,4]
     result = Solution.removeduplicate(nums)
     print(result)
        