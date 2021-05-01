"""
Problem 4: Dutch National Flag Problem

Version Date: April 12, 2021
"""


def swap(input_list, idx1, idx2):
    temp = input_list[idx1]
    input_list[idx1] = input_list[idx2]
    input_list[idx2] = temp


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    zero_idx, runner = 0, 0
    two_idx = len(input_list) - 1

    while runner <= two_idx:
        num = input_list[runner]

        if num is None:
            return "Invalid elements in array"

        if runner < zero_idx or num == 1:
            runner += 1
        elif num == 0:
            swap(input_list, runner, zero_idx)
            zero_idx += 1
        elif num == 2:
            swap(input_list, runner, two_idx)
            two_idx -= 1

    return input_list


def main():
    # Test Case 1 - Basic Operation
    print("Test Case 1 - Basic Operation")
    print(sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]))
    print('End of Test Case 1\n')

    # Test Case 2 - Basic Operation
    print("Test Case 2 - Basic Operation")
    print(sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]))
    print('End of Test Case 2\n')

    # Test Case 3 - Array already sorted
    print("Test Case 3 - Array already sorted")
    print(sort_012([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]))
    print('End of Test Case 3\n')

    # Test Case 4 - Null Input
    print("Test Case 4 - Null Input")
    print(sort_012([None]))
    print('End of Test Case 4\n')


if __name__ == '__main__':
    main()
