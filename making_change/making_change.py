#!/usr/bin/python

import sys

def making_change(amount, denominations):
  # Your code here
  # First pass: iterative, not recursive, but it may be faster this way.
  cache = [0 for i in range(amount + 1)]
  cache[0] = 1
  for den in denominations:
    for current in range(den, amount + 1):
      cache[current] += cache[current - den]
  return cache[-1]

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")