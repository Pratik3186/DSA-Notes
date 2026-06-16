from collections import defaultdict
class Solution:
    @staticmethod
    def numberofSubstring(s):
        left = 0
        count = 0
        freq = defaultdict(int)

        for right in range(len(s)):
            freq[s[right]] = freq[s[right]] + 1
            while len(freq) == 3:
                count = count+len(s)-right
                freq[s[left]] = freq[s[left]] - 1

                if freq[s[left]] == 0:
                    del freq[s[left]] 
                left = left+1
        return count


if __name__ == '__main__':
    s = 'abcabc'
    result = Solution.numberofSubstring(s)
    print(result)