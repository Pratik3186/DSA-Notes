def maxsum(nums,k):
    window = sum(nums[:k])
    max_sum = window
    for right in range(k,len(nums)):
        window = (window - nums[right -k] + nums[right])
        max_sum = max(window, max_sum)
    return max_sum / k

nums = [1,12,-5,-6,50,3]
k = 4
result = maxsum(nums,k)
print(result)