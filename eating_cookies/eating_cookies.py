'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, arr=None):
    # Your code here
    # # First pass: passes for small n, hangs for large
    # if arr != None:
    #     if arr[n] > 0:
    #         return arr[n]
    # if n <= 0:
    #     return 1
    # ways = 0
    # if n >= 3:
    #     ways += eating_cookies(n-3)
    # if n >= 2:
    #     ways += eating_cookies(n-2)
    # if n >= 1:
    #     ways += eating_cookies(n-1)
    # if arr != None:
    #     arr[n] = ways
    # return ways

    # # Second pass (iterative)
    # if n <= 1:
    #     return 1
    # if n == 2:
    #     return 2
    # if arr == None:
    #     arr = [0 for i in range(n+1)]
    # arr[0], arr[1], arr[2] = 1,1,2
    # for i in range(3,n+1):
    #     arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
    # return arr[n]

    # Alternate version with O(1) storage: ring cache
    # Initialize:
    cache = [1,1,2]
    count = 2 # == newest n
    oldest = 0 # == index of oldest returnable value
    if n < 3:
        return cache[n]
    while count < n:
        cache[oldest] = sum(cache)
        oldest = 0 if oldest == 2 else oldest + 1
        count += 1
    return cache[oldest-1]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
