class Solution:
    @staticmethod
    def numRescueBoat(people,limit):
        people.sort()
        left = 0
        right = len(people)-1
        boat = 0
        while left<=right:
            if people[left] + people[right] <= limit:
                left+=1
            right-=1
            boat+=1
        return boat
    
if __name__ == '__main__':
    people = [3,5,3,4]
    limit = 3
    result = Solution.numRescueBoat(people,limit)
    print(result)
