#Trapping Rain Water 
class Solution:
    @staticmethod
    def trapwater(heights):
        left = 0
        n = len(heights)
        right = n-1

        leftmax = 0
        rightmax = 0
        water = 0
        while left<right:
            if heights[left] < heights[right]:
                if heights[left] >= leftmax:
                    leftmax = heights[left]
                else:
                    water = water+leftmax-heights[left]
                left+=1
            else:
                if heights[right] > rightmax:
                    rightmax = heights[right]
                else:
                    water = water + rightmax - heights[right]
                right -=1 
        return water


if __name__ == '__main__':
    heights = [4,2,0,3,2,5]
    result = Solution.trapwater(heights)
    print(result)

