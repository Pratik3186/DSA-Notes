#165. Compare version number ]
class Solution:
    @staticmethod 
    def compareversionNumber(v1,v2):
        i = 0
        j = 0
        p = len(v1)
        q = len(v2)
        while i< p or j < q:
            nums1 = 0
            while i < p and v1[i] != '.':
                nums1 = nums1*10 + int(v1[i])
                i+=1
            nums2 = 0
            while j< q and v2[j] != '.':
                nums2 = nums2*10 + int(v2[j])
                j+=1
            if nums1 < nums2:
                return -1
            elif nums1>nums2:
                return 1
            i+=1
            j+=1
        return 0 
    
if __name__ == '__main__':
    v1 = '1.2.3.4.3.2'
    v2 = '1.2.3.5.4.2'
    result = Solution.compareversionNumber(v1,v2)
    print(result)
