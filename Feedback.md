## Setup

### Dataset, Libraries, and Setup

- On my computer, I needed to run all commands as python3 instead of python, we may want to note this in case other users encounter this.

### Python Installation

- This should come before Dataset, Libraries, and Setup since it relies on Python to be installed.
- Setting environment variables (step 6) should come after step 3. 

### Python Libraries Installation

- I had to use python3 -m pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl to install tensorflow on my mac
- Spacy seems to not support mac
- We also don't seem to use any of these libraries, so it might be best to not install them

## Milestone 1

For advanced features, we say: Optimize Search for Large File Lists
    - We cannot exit early since the search example acts as a filter, find all x with y attribute. Early termination would work for finding a set number of instances of an item.

The solution doesn't handle the case where an attribute doesn't exist for the search object

## Milestone 2

It might be nice to show both the recursive and iterative approach in the solution

## Milestone 3

In the sample project, in selection_sort.py, there are two return file_records lines