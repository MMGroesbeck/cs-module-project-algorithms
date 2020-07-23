#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # Your code here
  # First pass: works as instructed.
  if n < 1:
    return [[]]
  if n == 1:
    return [["rock"], ["paper"], ["scissors"]]
  else:
    child = rock_paper_scissors(n-1)
    out = []
    for i in child:
      out.append(i + ["rock"])
      out.append(i + ["paper"])
      out.append(i + ["scissors"])
    return out

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')