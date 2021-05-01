"""
Problem 2: Search in a Rotated Sorted Array

Version Date: April 8, 2021
"""


def rotated_array_search(arr, target):
    """
    Find the index by searching in a rotated sorted array

    Args:
       arr(array) Input array to search,
       target(int):  The target
    Returns:
       int: Index or -1
    """

    # different flavor of binary search,
    # trick is that we identify the strictly inc half, and then inc pointers from there

    if not isinstance(target, int):
        return "Target must be an integer."

    # initialize variables
    n = len(arr)
    start = 0
    end = n - 1

    # start the binary search
    while start <= end:
        # from here we will evaluate whether the target is in second half or first
        mid = (start + end)//2

        # if target is the mid element, then return the mid element
        if arr[mid] == target:
            return mid

        # else if mid element is greater than the starting element, then left half is the strictly inc part
        elif arr[mid] >= arr[start]:
            # if target is within the the left half, set the end to the mid - 1
            if (target >= arr[start]) and (target <= arr[mid]):
                end = mid - 1
            # else, target is not in left half so set the start to mid + 1
            else:
                start = mid + 1
        # else, the right half is the increasing part
        else:
            # if the target is within the right half, set the start to mid + 1
            if (target >= arr[mid]) and (target <= arr[end]):
                start = mid + 1
            # else, target is not within right half so set the end to mid - 1
            else:
                end = mid - 1
    # return -1 if target not here
    return -1


def main():
    # Test Case 1 - Target in array
    print("Test Case 1 - Target in Array")
    print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6), "(we expect answer to be 0)")
    print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8), "(we expect answer to be 2)")
    print('End of Test Case 1\n')

    # Test Case 2 - Target not in array
    print("Test Case 2 - Target not in array")
    print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 20), "(we expect answer to be -1)")
    print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], -1), "(we expect answer to be -1)")
    print('End of Test Case 2\n')

    # Test Case 3 - Target not integer
    print("Test Case 3 - Target not integer")
    print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], "Hi"))
    print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], None))
    print('End of Test Case 3\n')


if __name__ == '__main__':
    main()
