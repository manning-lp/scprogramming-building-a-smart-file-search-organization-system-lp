"""
optimized_sort.py

In this module, we demonstrate an optimized sorting approach, typically 
using Python's built-in sort (Timsort) or other advanced algorithms 
like Merge Sort or Quick Sort.

Theory and Explanation:
-----------------------
1. Python's built-in `sort()` uses Timsort with an average O(n log n) complexity.
2. Much faster than O(n^2) Selection Sort for larger datasets.
3. You could also implement Merge Sort or Quick Sort here to compare performance.

Milestone 4 (Guidance):
-----------------------
Explore optimization techniques for sorting large datasets. 
Compare Selection Sort with this optimized approach.

Implementation Hints:
---------------------
- Accept a list of items (file_records) and the attribute to sort by.
- Simply call file_records.sort(key=lambda x: x[attribute]) 
  or use the built-in 'sorted(file_records, key=lambda...)'.
- Compare performance with Selection Sort for large data.
"""

def optimized_sort(file_records, attribute):
   file_records.sort(key=lambda record: getattr(record, attribute))
   return file_records
