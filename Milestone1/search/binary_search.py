
"""
binary_search.py

In this module, we will implement the Binary Search algorithm.

Theory and Explanation:
-----------------------
1. Binary Search is an efficient searching algorithm for sorted arrays/lists.
2. It compares the target value to the middle element:
   - If not equal, it decides which half to search next (because data is sorted).
3. Time Complexity: O(log n).

Why Binary Search?
------------------
- Much faster than Linear Search for large sorted datasets.
- Requires the data to be sorted beforehand by the search attribute.

Milestone 2 (Guidance):
-----------------------
Enhance your search system by integrating Binary Search. 
Remember the data must be sorted first by the same attribute.

Implementation Hints:
---------------------
- Accept a sorted list of items by a given attribute.
- Use two pointers (left = 0, right = len(list) - 1).
- While left <= right:
  * mid = (left + right) // 2
  * Compare the 'mid' element with 'value'.
  * If smaller, move left pointer; if larger, move right pointer.
- Handle duplicates if you want all matches.

Below is a skeleton code with detailed comments.
"""

def binary_search_rec(arr, attribute, value, low, high):
    if low > high:
        return False 
    else:
        mid = (low + high) // 2 
        if value == getattr(arr[mid],attribute):
            return mid
        elif value > getattr(arr[mid], attribute):
            return binary_search_rec(arr, attribute, value, mid + 1, high)
        else:
            return binary_search_rec(arr, attribute, value, low, mid - 1)

def binary_search(file_records, attribute, value):
   return binary_search_rec(file_records, attribute, value, 0, len(file_records))
   
