#3Sum Closest
class Solution:
    @staticmethod
    def threeSumClosest(nums,target):
        nums.sort()
        # result = []
        best = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left<right:
                total = nums[i]+nums[left]+nums[right]
                if abs(target-total)< abs(best-total):
                    best = total
                if target<total:
                    right-=1

                elif target>total:
                    left+=1
                else:
                    return target
        return best
if __name__ == '__main__':
    nums = [-1,2,1,-4]
    target = 1
    result = Solution.threeSumClosest(nums,target)
    print(result)
                
                