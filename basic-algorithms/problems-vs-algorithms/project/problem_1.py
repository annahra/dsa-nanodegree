"""
Problem 1: Finding the Square Root of an Integer

Version Date: April 7, 2021

Will only evaluate positive integers. If a negative integer is inputed,
the algorithm will return None.
"""


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 2:
        return number

    lower_bound = 0
    upper_bound = number

    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) //2

        if mid * mid <= number < (mid + 1)*(mid + 1):
            return mid
        elif number < mid * mid:
            upper_bound = mid
        else:
            lower_bound = mid


def main():
    # Test Case 1 - Perfect Squares
    print("Test Case 1 - Perfect Squares")
    print("The square root of 9 is", sqrt(9), "(expect 3)")
    print("The square root of 0 is", sqrt(0), "(expect 0)")
    print("The square root of 1 is", sqrt(1), "(expect 1)")
    print("The square root of 16 is", sqrt(16), "(expect 4)")
    print('End of Test Case 1\n')

    # Test Case 2 - Non-squareable numbers
    print("Test Case 2 - Non-squareable numbers")
    print("The floored square root of 27 is", sqrt(27), "(expect 5)")
    print("The floored square root of 15 is", sqrt(15), "(expect 3)")
    print("The floored square root of 8 is", sqrt(8), "(expect 2)")
    print('End of Test Case 2\n')

    # Test Case 3 - Negative Numbers
    print("Test Case 3 - Negative Numbers")
    print("The floored square root of -1 is", sqrt(-1), "(expect None)")
    print("The floored square root of -16 is", sqrt(-16), "(expect None)")
    print('End of Test Case 3\n')

    # Test Case 4 - Large Numbers
    print("Test Case 4 - Large Numbers")
    print("The floored square root of -1 is", sqrt(99960004), "(expect 9998)")
    print('End of Test Case 4\n')


if __name__ == '__main__':
    main()
