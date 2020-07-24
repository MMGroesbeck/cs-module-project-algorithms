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

# def sliding_window_max(nums, k):
#     for i in range(len(nums)-k+1):
#         r = min(i+k, len(nums))
#         nums[i] = max(nums[i:r])
#     return nums[:len(nums)-k+1]
# # Even slower

# # Recursive:
# def sliding_window_max(nums, k, root=True):
#     if len(nums) < 1:
#         return []
#     nums[0] = max(nums[:k])
#     rest = sliding_window_max(nums[1:], k, False)
#     if root:
#         # return [nums[:len(nums)-k+1]]
#         return [nums[0]] + rest[:len(nums)-k]
#     else:
#         return [nums[0]] + rest
# # Also too slow.

# # Proof of concept:
# def sliding_window_max(nums, k):
#     window = nums[:k-1]
#     arr = []
#     for i in range(len(nums)-k+1):
#         window.append(nums[i+k-1])
#         window.sort()
#         arr.append(window[-1])
#         window.remove(nums[i])
#     return arr
# # Too slow, but should clarify index issues

# import math

# def sliding_window_max(nums, k):
#     window = sorted(nums[:k-1])
#     out_arr = []
#     def win_ins(win, target, start=0, end=k-2):
#         if target <= win[start]:
#             win.insert(start, target)
#         elif target >= win[end]:
#             win.append(target)
#         else:
#             mid = math.floor((start + end)/2)
#             if win[mid] == target:
#                 win.insert(mid, target)
#             elif mid == start or mid == end:
#                 win.insert(end, target)
#             else:
#                 if target < win[mid]:
#                     win_ins(win, target, start, mid)
#                 else:
#                     win_ins(win, target, mid, end)
#     for i in range(len(nums)-k+1):
#         win_ins(window, nums[i+k-1])
#         out_arr.append(window[-1])
#         window.remove(nums[i])
#     return out_arr
# # Still over 8 seconds; is .remove() slow?

# import math

# def sliding_window_max(nums, k):
#     window = sorted(nums[:k-1])
#     out_arr = []
#     def get_ind(win, target, start=0, end=k-2):
#         if target <= win[start]:
#             return start
#         elif target >= win[end]:
#             return end
#         else:
#             mid = math.floor((start + end)/2)
#             if win[mid] == target:
#                 return mid
#             elif mid == start:
#                 return start
#             elif mid == end:
#                 return end
#             else:
#                 if target < win[mid]:
#                     return get_ind(win, target, start, mid-1)
#                 else:
#                     return get_ind(win, target, mid+1, end)
#     def win_ins(target):
#         nonlocal window
#         if target >= window[-1]:
#             window.append(target)
#         else:
#             window.insert(get_ind(window, target), target)
#     def win_del(target):
#         nonlocal window
#         x = get_ind(window, target, 0, k-1)
#         window = window[:x]+window[x+1:]
#     for i in range(len(nums)-k+1):
#         win_ins(nums[i+k-1])
#         out_arr.append(window[-1])
#         win_del(nums[i])
#     return out_arr
#     # Still slow AND broken

# def sliding_window_max(nums, k):
#     leng = len(nums)
#     out_arr = [None for i in range(leng)]
#     for i in range(leng):
#         curr = max(leng - i - k, 0)
#         while curr < leng and curr < leng-i-1 and (out_arr[curr] == None or out_arr[curr] < nums[curr]):
#             out_arr[curr] = nums[curr]
#             curr += 1
#     return out_arr[:leng - k]
#  # Broken -- check indices

# def sliding_window_max(nums, k):
#     leng = len(nums)
#     out_arr = [None for i in range(leng)]
#     for i in range(leng):
#         curr = max(0, leng-i-k)
#         this_item = nums[leng-i-1]
#         while curr < leng-i and (out_arr[curr] == None or out_arr[curr] < this_item):
#             out_arr[curr] = this_item
#             curr += 1
#     return out_arr[:leng-k+1]
# # Under 2 seconds -- major improvement!

# Rough mock-up of deque
def sliding_window_max(nums, k):
    out_arr = []
    deque = []
    def deque_add(ind):
        nonlocal deque
        while len(deque) > 0 and nums[deque[-1]] < nums[ind]:
            deque.pop()
        deque.append(ind)
    def deque_maint(new_ind):
        while deque[0] < new_ind:
            deque.pop(0)
    for i in range(k):
        deque_add(i)
    for i in range(len(nums)-k+1):
        deque_add(i+k-1)
        deque_maint(i)
        out_arr.append(nums[deque[0]])
    return out_arr
# Passes!
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
