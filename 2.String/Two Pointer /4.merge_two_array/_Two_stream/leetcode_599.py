class Solution:
    @staticmethod 
    def minimumIndexSum(list1,list2):
        position = {}
        for index,restaurant in enumerate(list2):
            position[restaurant] = index

        answer = []
        minimum_sum = float('inf')
        for i,restaurant in enumerate(list1):
            if restaurant in position:
                index_sum = i + position[restaurant]

                if index_sum < minimum_sum:
                    minimum_sum = index_sum
                    answer = [restaurant]
                elif index_sum == minimum_sum:
                    answer.append(restaurant)
        return answer 
    
if __name__ == '__main__':
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"] 
    list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
    result = Solution.minimumIndexSum(list1,list2)
    print(result)
    
