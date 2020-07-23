#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

# def knapsack_solver(items, capacity):
#   # items is a list of Items
#   # Returns: {'Value': int, 'Chosen': [list of item indices]}
#   # Your code here
#   # First try: top-down recursive exploration of *all* possible selection combinations
#   # Dict 'options' holds possibilities for next item chosen in ready-to-return format
#   # 'Null' option represents no further items to choose.
#   options = {'Null':{'Value': 0, 'Chosen': []}}
#   for item in items:
#     # Iterate through possible items to choose next
#     if item.size <= capacity:
#       # If item can fit, find selections and max value for other items and reduced capacity
#       # Only higher indices used in recursion to prevent duplication (e.g. 1 then 2 vs 2 then 1)
#       # This reduces runtime by ~half and implicitly sorts
#       sub_selection = knapsack_solver([i for i in items if i.index < item.index], capacity-item.size)
#       sub_selection['Chosen'].append(item.index)
#       sub_selection['Value'] += item.value
#       options.update({item.index: sub_selection})
#   # Determine option with maximum value to pass back to parent
#   max_val = 'Null'
#   for key in options.keys():
#     if options[key]['Value'] > options[max_val]['Value']:
#       max_val = key
#   return options[max_val]
#   # Passes for small, slow for medium and large.
#   # Compares *all* possible ways to fill the pack
#   # TO DO: improve runtime, get storage at least somewhat under control

# Second pass: add item with highest value per unit size that fits in remaining space
# This will NOT always give the optimum solution, just a quick estimate
def knapsack_solver(items, capacity, sorted=False):
  if sorted == False:
    # Sort items by descending "value density"; selection sort here for simplicity
    # Sort only triggers once
    for i in range(0, len(items) - 1):
      smallest_index = i
      for j in range(i + 1, len(items)):
        if (items[j].value/items[j].size) > (items[smallest_index].value/items[smallest_index].size):
          smallest_index = j
      if smallest_index != i:
        items[i], items[smallest_index] = items[smallest_index], items[i]
  for i in range(len(items)):
    if items[i].size <= capacity:
      # Only the first (most value-dense) item which will fit triggers the next recursion:
      sub_selection = knapsack_solver(items[1:], capacity-items[i].size, True)
      sub_selection['Chosen'].append(items[i].index)
      chosen_items = sub_selection['Chosen']
      sub_selection['Chosen'].sort()
      sub_selection['Value'] += items[i].value
      return sub_selection
  return {'Value': 0, 'Chosen': []}
  # Passes test for medium size, fails for large;
  # For large, returns a solution with Value = 2639 instead of 2640
  # But it takes ~ .09 seconds even for the large version!
  # This estimate is only O(n) runtime complexity, instead of O(2^n)

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')