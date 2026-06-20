from typing import List
class Solution:
    @staticmethod
    def container(heights):
        left = 0
        right = len(heights)-1
        max_water = 0
        while left<right:
            width = right - left
            current_height = min(heights[left], heights[right])
            area = width*current_height
            max_water = max(max_water,area)
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return max_water
    
if __name__== '__main__':
    heights = [1,8,6,2,5,4,8,3,7]
    result = Solution.container(heights)
    print(result)