'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# # First pass: O(n*k); runs O(n) for small k, but can be improved.
# # Will need data structure for window with O(1) add/remove for each i
# def sliding_window_max(nums, k):
#     # Your code here
#     out_arr = []
#     for i in range(len(nums) - k + 1):
#         out_arr.append(nums[i])
#         for j in range(1,k):
#             if len(nums) > i + j:
#                 if nums[i+j] > out_arr[i]:
#                     out_arr[i] = nums[i+j]
#     return out_arr

# # Second pass, ring buffer:
# def sliding_window_max(nums, k):
#     frame = [nums[i] for i in range(k)]
#     frame_max = max(frame)
#     for i in range(len(nums) - k + 1):
#         nums[i] = frame_max
#         if i < len(nums) - k:
#             x = frame.pop(0)
#             frame.append(nums[i+k])
#             frame_max = max(frame)
#     return nums[:len(nums)-k+1]
# # Fails on time: takes over 8 seconds for large n and k

# # Third pass, better ring buffer:
# def sliding_window_max(nums, k):
#     frame = [nums[i] for i in range(k)]
#     oldest = 0
#     frame_max = max(frame)
#     for i in range(len(nums) - k + 1):
#         nums[i] = frame_max
#         if i < len(nums) - k:
#             frame[oldest] = nums[i+k]
#             if oldest == k-1:
#                 oldest = 0
#             else:
#                 oldest += 1
#             frame_max = max(frame)
#     return nums[:len(nums)-k+1]
# # Still over 8 seconds. Updating frame_max only when item removed from frame == frame_max did not improve.

# # Another approach:
# def sliding_window_max(nums, k):
#     for i in range(len(nums)):
#         for j in range(k):
#             if i-j >= 0 and i-j <= len(nums)-k:
#                 if nums[i] > nums[i-j]:
#                     nums[i-j] = nums[i]
#     return nums[:len(nums)-k+1]
# # Still too slow.

def sliding_window_max(nums, k):
    for i in range(len(nums)-k+1):
        r = min(i+k, len(nums))
        nums[i] = max(nums[i:r])
    return nums[:len(nums)-k+1]
# Even slower
    

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
