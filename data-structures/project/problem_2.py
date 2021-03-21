"""
Problem 2: File Recursion
Author: Annah Ramones

Version Date: March 16, 2021

The following cases are commented out because we expect errors to be thrown:
- Last case of Test Case 2
- All cases of Test Case 3

Please uncomment each individual case to test
"""

import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix of the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if not os.path.isdir(path):
        raise Exception("Directory does not exist in this path")

    if suffix == "" or type(suffix) is not str:
        raise Exception("Invalid extension type")

    # base case: empty directory
    if len(os.listdir(path)) == 0:
        return []

    # get all content in directory
    directory_contents = os.listdir(path)

    result_list = []

    folder_list = []

    # iterate through contents checking for file with extension, add to result_list. get all folders
    for item in directory_contents:
        rel_path = path + "/" + item
        if os.path.isfile(rel_path):
            if rel_path.endswith(suffix):
                result_list.append(rel_path)
        elif os.path.isdir(rel_path):
            folder_list.append(rel_path)

    # iterate through folders, call recursive function
    for folder in folder_list:
        # extend result_list to include returned files
        result_list.extend(find_files(suffix, folder))

    return result_list


def main():
    # Test Case 1 - Basic Functionality
    print("Test Case 1 - Basic Function")
    print('Ends with .c: ', find_files(".c", "./testdir"))  # we expect 4 files with .c suffix
    print('Ends with .gitkeep: ', find_files(".gitkeep", "./testdir"))  # we expect 2 files with .gitkeep suffix
    print('End of Test Case 1\n')

    # Test Case 2 - No such file with extension, or no such directory
    print("Test Case 2 - No such file with extension, or no such directory")
    print('No file with extension: ', find_files(".a", "./testdir"))  # we expect an empty list
    # print('Test Case 2: ', find_files(".a", "./testdi"))  # we expect an exception saying "Directory does not exist in this path"
    print('End of Test Case 2\n')

    # Test Case 3 - Invalid extension inputs
    print("Test Case 3 - Invalid extension inputs, uncomment cases")
    # print('Test Case 3: ', find_files("", "./testdir"))     # we expect an exception saying "Invalid extension type"
    # print('Test Case 3: ', find_files(2, "./testdir"))      # we expect an exception saying "Invalid extension type"
    # print('Test Case 3: ', find_files([], "./testdir"))     # we expect an exception saying "Invalid extension type"


if __name__ == "__main__":
    main()
