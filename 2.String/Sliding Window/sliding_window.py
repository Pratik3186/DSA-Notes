def fixed_window(arr, k):
    # First window
    window_sum = sum(arr[:k])

    # Answer initialization
    ans = window_sum

    # Slide window
    for right in range(k, len(arr)):
        window_sum += arr[right]      # Add new element
        window_sum -= arr[right - k]  # Remove old element

        ans = max(ans, window_sum)    # Update answer

    return ans

# arr = [2, 1, 5, 1, 3, 2]
arr = [1,2,3,4,5,6,7]
k = 3

print(fixed_window(arr, k))