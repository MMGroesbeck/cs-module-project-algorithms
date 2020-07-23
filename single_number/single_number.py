'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

# # First run: nested for loops
# # Inner loop needs to be over whole range to catch matches before current number.
# def single_number(arr):
#     # Your code here
#     for i in range(len(arr)-1):
#         match = False
#         for j in range(len(arr)):
#             if i != j and arr[i] == arr[j]:
#                 match = True
#         if match == False:
#             return arr[i]

# Second run: group version (O(n) runtime, one pass, but memory is based on size of set.)
# There seems to be a tradeoff between runtime and storage complexity
def single_number(arr):
    found = set()
    for x in arr:
        if x in found:
            found.remove(x)
        else:
            found.add(x)
    return list(found)[0]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")