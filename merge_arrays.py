#!/usr/bin/env python

import sys

def merge_sorted_arrays(arr1, arr2):
  merged_arr = []
  arr2_length = len(arr2)
  arr1_length = len(arr1)

  while arr2 and arr1:
    # for every item for arr2, find position and insert on arr1
    if arr2[0] == arr1[0]:
      merged_arr.append(arr1.pop(0))
      arr2.pop(0)
    elif arr1[0] < arr2[0]:
      merged_arr.append(arr1.pop(0))
    else:
      merged_arr.append(arr2.pop(0))

  if arr1:
    merged_arr.extend(arr1)
  if arr2:
    merged_arr.extend(arr2)

  print merged_arr
  return merged_arr

if (__name__ == "__main__"):
  try:
    merge_sorted_arrays([1,2], [3,4])
    merge_sorted_arrays([1,4], [2,3])
    merge_sorted_arrays([1,4,5], [2,3])
  except:
    print 'Usage: python file_name.py <n>'
