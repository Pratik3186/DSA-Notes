#Remove Element 
class Solution:
    @staticmethod
    def removeElement(nums,val):
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow+=1
        return slow
    

if __name__ == '__main__':
    nums = [3,2,2,3]
    val = 3
    result = Solution.removeElement(nums,val)
    print(result)
                
        