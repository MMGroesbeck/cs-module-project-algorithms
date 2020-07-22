#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  # items is a list of Items
  # Returns: {'Value': int, 'Chosen': [list of item indices]}
  # Your code here
  # First try: top-down recursive exploration of *all* possible selection combinations
  # Dict 'options' holds possibilities for next item chosen in ready-to-return format
  # 'Null' option represents no further items to choose.
  options = {'Null':{'Value': 0, 'Chosen': []}}
  for item in items:
    # Iterate through possible items to choose next
    if item['size'] <= capacity:
      # If item can fit, find selections and max value for other items and reduced capacity
      # Only higher indices used in recursion to prevent duplication (e.g. 1 then 2 vs 2 then 1)
      # This reduces runtime complexity and implicitly sorts
      sub_selection = knapsack_solver([i for i in items if i['index'] < item['index']], capacity-item['size'])
      sub_selection['Chosen'].append(item['index'])
      sub_selection['Value'] += item['value']
      options.update({item['index']: sub_selection})
  # Determine option with maximum value to pass back to parent
  # TO DO: improve runtime, get storage at least somewhat under control
  max_val = 'Null'
  for key in options.keys():
    if options[key]['Value'] > options[max_val]['Value']:
      max_val = key
  return options[max_val]
  

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