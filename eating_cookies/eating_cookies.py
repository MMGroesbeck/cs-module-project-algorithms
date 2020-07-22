'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, arr=None):
    # Your code here
    # First pass: passes for small n, hangs for large
    if arr != None:
        if arr[n] > 0:
            return arr[n]
    if n <= 0:
        return 1
    ways = 0
    if n >= 3:
        ways += eating_cookies(n-3)
    if n >= 2:
        ways += eating_cookies(n-2)
    if n >= 1:
        ways += eating_cookies(n-1)
    if arr != None:
        arr[n] = ways
    return ways

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
