class Solution:
    @staticmethod
    def stringCompression(chars):
        slow = 0
        fast = 0
        n = len(chars)
        while fast<n:
            current = chars[fast]
            count = 0
            while fast<n and chars[fast] == current:
                fast +=1
                count+=1
            chars[slow] = current
            slow+=1
            if count>1:
                for digit in str(count):
                    chars[slow] = digit
                    slow+=1 
        return slow
    
if __name__ == '__main__':
    chars = ['a','a','b','b','c','c','c']
    result = Solution.stringCompression(chars)
    print(chars[:result])
    

