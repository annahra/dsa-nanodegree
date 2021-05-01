"""
Problem 6: Max and Min in an Unsorted Integer Array

Version Date: April 14, 2021
"""
import random
import sys


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None

    min_num = sys.maxsize
    max_num = sys.maxsize * -1

    for num in ints:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num

    return min_num, max_num


def main():
    # Test Case 1 - Basic Operation
    print("Test Case 1 - Basic Operation")
    num_list = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(num_list)
    print("Min and max of", num_list)
    print(get_min_max(num_list))
    print('End of Test Case 1\n')

    # Test Case 2 - Negative Numbers
    print("Test Case 2 - Negative Numbers")
    num_list = [i for i in range(-50, 51)]  # a list containing -50 - 50
    random.shuffle(num_list)
    print("Min and max of", num_list)
    print(get_min_max(num_list))
    print('End of Test Case 2\n')

    # Test Case 3 - Empty List
    print("Test Case 3 - Empty List")
    num_list = []  # a list containing nothing
    print("Min and max of", num_list)
    print(get_min_max(num_list))
    print('End of Test Case 3\n')


if __name__ == '__main__':
    main()
