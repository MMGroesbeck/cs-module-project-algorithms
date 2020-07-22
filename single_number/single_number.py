'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

# First run: nested for loops
# Inner loop needs to be over whole range to catch matches before current number.
def single_number(arr):
    # Your code here
    for i in range(len(arr)-1):
        match = False
        for j in range(len(arr)):
            if i != j and arr[i] == arr[j]:
                match = True
        if match == False:
            return arr[i]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")