'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# First pass: O(n*k); runs O(n) for small k, but can be improved.
def sliding_window_max(nums, k):
    # Your code here
    out_arr = []
    for i in range(len(nums) - k + 1):
        out_arr.append(nums[i])
        for j in range(1,k):
            if len(nums) > i + j:
                if nums[i+j] > out_arr[i]:
                    out_arr[i] = nums[i+j]
    return out_arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
