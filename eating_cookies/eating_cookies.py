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

    # # Second pass: iterative, O(n) runtime, O(n) storage
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

    # # Alternate version with O(n) runtime, O(1) storage: ring cache
    # # Initialize:
    # cache = [1,1,2]
    # count = 2 # == newest n
    # oldest = 0 # == index of oldest returnable value
    # if n < 3:
    #     return cache[n]
    # while count < n:
    #     cache[oldest] = sum(cache)
    #     oldest = 0 if oldest == 2 else oldest + 1
    #     count += 1
    # return cache[oldest-1]

    # # Just because: O(1) storage, runtime same order as computing c^n:
    # # eating_cookies(n) is the (n+1)th Tribonacci number, so:
    # def trib(n):
    #     a_plus = (19 + (3 * (33 ** (1/2))))**(1/3)
    #     a_minus = (19 - (3 * (33 ** (1/2))))**(1/3)
    #     b = (586 + (102 * (33 ** (1/2))))**(1/3)
    #     top = ((1/3)*(a_plus + a_minus + 1))**n
    #     bottom = (b**2) - (2*b) + 4
    #     return round(3 * b * top / bottom)
    # return trib(n+1)
    # # Gives rounding errors starting with n=54
    # # Gives overflow errors with very large n (definitely by 10k)
    # # At n=10k, though, runtime for the previous version is still ~5ms

    # Cache + recursion:
    if arr == None:
        arr = [0 for i in range(n+1)]
        arr[0] = 1
    if n < 0:
        return 0
    if n == 0:
        return 1
    elif arr[n] > 0:
        return arr[n]
    else:
        arr[n] = eating_cookies(n-1, arr) + eating_cookies(n-2, arr) + eating_cookies(n-3, arr)
        return arr[n]
    # Uses O(n) storage, though that storage may be passed in as an array of zeroes


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
