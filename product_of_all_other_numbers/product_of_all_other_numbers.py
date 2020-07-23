'''
Input: a List of integers
Returns: a List of integers
'''

# # First pass is in O(n) time and O(1) space, but uses division.
# def product_of_all_other_numbers(arr):
#     # Your code here
#     # First version uses division
#     prod = 1
#     for n in arr:
#         prod *= n
#     return[prod / n for n in arr]

# Second pass:
import math
def product_of_all_other_numbers(arr):
    prod_arr = [1 for i in range(len(arr))]
    for i in range(len(arr)):
        x = arr.pop(i)
        prod_arr[i] = math.prod(arr)
        arr.insert(i,x)
    return prod_arr
# O(n) space; time complexity depends on whether math.prod() runs an iterative loop behind the scenes

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
