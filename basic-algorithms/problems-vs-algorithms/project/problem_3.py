"""
Problem 3: Rearrange Array Elements

Version Date: April 9, 2021

I chose to represent the numbers as strings so that I could catch the last test case (0's and 1's)
If I represented the numbers using an integer, then the answer to test case 3 would be [100,0] which
violates one of the rules that the length of the digits cannot be more than 1.
"""


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def rearrange_digits(arr):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       arr(array): Input array
    Returns:
       (int),(int): Two maximum sums
    """
    n = len(arr) - 1

    arr = mergesort(arr)

    first_number = ""
    second_number = ""

    for i in range(n + 1):
        if i % 2 == 0:
            first_number += str(arr[i])
        else:
            second_number += str(arr[i])

    return [first_number, second_number]


def main():
    # Test Case 1 - Basic Operation
    print("Test Case 1 - Basic Operation")
    print(rearrange_digits([1, 2, 3, 4, 5]))
    print('End of Test Case 1\n')

    # Test Case 2 - Basic Operation
    print("Test Case 2 - Basic Operation")
    print(rearrange_digits([4, 6, 2, 5, 9, 8]))
    print('End of Test Case 2\n')

    # Test Case 3 - Zeroes and Ones
    print("Test Case 3 - Zeroes and Ones")
    print(rearrange_digits([0, 0, 1, 0, 0]))
    print('End of Test Case 3\n')


if __name__ == '__main__':
    main()
