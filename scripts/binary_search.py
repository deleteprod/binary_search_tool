#!/usr/bin/env python3

'''
Binary search (also known as half-search or logarithmic search) example.
See wiki page for more details - https://en.wikipedia.org/wiki/Binary_search_algorithm
'''

def binary_search(list, item):
    low = 0
    high = len(list) - 1

# While loop to step through guesses chopping off half of all possibilities each time
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else: low = mid + 1
    return None

# Generate a list to search
the_list = [1, 3, 5, 7, 9]

# Example - return the index in the_list where the value 3 exists
print(binary_search(the_list, 3))

# Example - attempt to find the index where -1 is the value - returns None
print(binary_search(the_list, -1))
