class Solution:
    @staticmethod
    def mergeAlternative(word1,word2):
        i = 0
        j = 0
        result = []
        while i< len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i+=1
            j+=1
        while i<len(word1):
            result.append(word1[i])
            i+=1
        while j<len(word2):
            result.append(word2[j])
            j+=1
        return ''.join(result)
    
if __name__ == '__main__':
    word1 = 'abc'
    word2 = 'pqrs'
    result = Solution.mergeAlternative(word1,word2)
    print(result)