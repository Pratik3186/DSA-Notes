class Solution:
    @staticmethod
    def twoSumII(numbers,target):
        left = 0
        right= len(numbers) -1 
        while left< right:
            total = numbers[left] + numbers[right]
            if total < target:
                left += 1
            elif total> target:
                right -=1
            else:
                return [left+1,right+1]
            
if __name__ == '__main__':
    numbers = [2,7,11,15]
    target = 9
    result = Solution.twoSumII(numbers,target)
    print(result)
