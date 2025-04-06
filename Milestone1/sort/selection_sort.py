"""
selection_sort.py

In this module, we will implement the Selection Sort algorithm.

Theory and Explanation:
-----------------------
1. Selection Sort is a simple sorting algorithm.
2. It finds the minimum element in the unsorted part of the list 
   and swaps it with the element at the beginning of that part.
3. Time Complexity: O(n^2).

Why Selection Sort?
-------------------
- Conceptually simple and easy to follow.
- Not efficient for large datasets, but good for demonstration.

Milestone 3 (Guidance):
-----------------------
Implement a function to sort files by attributes (e.g., name, size, date)
using Selection Sort.

Implementation Hints:
---------------------
- Accept a list and the attribute to sort by.
- For i in range(len(list)):
  * Set min_index = i
  * For j in range(i+1, len(list)):
    - If file_records[j][attribute] < file_records[min_index][attribute],
      update min_index
  * Swap items at i and min_index.

Below is a skeleton code with detailed comments.
"""

def selection_sort(file_records, attribute):
    size = len(file_records)
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if getattr(file_records[i], attribute) < getattr(file_records[min_idx], attribute):
                min_idx = i
         
        # put min at the correct position
        (file_records[step], file_records[min_idx]) = (file_records[min_idx], file_records[step])
    return file_records
    
