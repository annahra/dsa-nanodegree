"""
Problem 4: Active Directory
Author: Annah Ramones

Version Date: March 17, 2021

Test Case 3 is commented out because we expect a ValueError to be thrown for each case.

"""


class Group(object):
    def __init__(self, _name):
        if _name == "" or _name is None:
            raise ValueError("Invalid Group Name")
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        if type(group) is not Group:
            raise ValueError("Not a valid group")
        self.groups.append(group)

    def add_user(self, user):
        if user == "" or user is None:
            raise ValueError("Invalid User Name")
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def find_user(user, group):
    # base case, group has no users and no sub groups
    if len(group.get_groups()) == 0 and len(group.get_users()) == 0:
        return ""

    # iterate through user list to find users
    for current_user in group.get_users():
        if user == current_user:
            return current_user

    result = ""
    # iterate through groups, call self on each group
    for current_group in group.get_groups():
        result += find_user(user, current_group)

    # if we get here, we haven't found user still
    return result


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if type(group) is not Group:
        raise ValueError("Not a valid group")

    if type(user) is not str:
        raise ValueError("Not a valid user")

    user_name = find_user(user, group)
    if user_name == "":
        return False

    return True


def main():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")
    sub_child2 = Group("subchild2")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    child.add_group(sub_child2)
    parent.add_group(child)

    # Test Case 1: Basic Function
    print("Test Case 1 - Basic Function")
    print("Is Sub Child User apart of Parent (true):", is_user_in_group(sub_child_user, parent))
    print("Is Sub Child User apart of Child (true):", is_user_in_group(sub_child_user, child))
    print("Is Sub Child User apart of Sub Child (true):", is_user_in_group(sub_child_user, sub_child))
    print('End of Test Case 1\n')

    # Test Case 2: Not in Group
    print("Test Case 2 - Not in Group")
    print("Is Sub Child User apart of Sub Child 2 (false):", is_user_in_group(sub_child_user, sub_child2))
    print("Is this nonexistent user apart of Parent (false):", is_user_in_group("random user", parent))
    print('End of Test Case 2\n')

    # Test Case 3: Invalid group and user
    print("Test Case 3 - Invalid group and user, uncomment cases")
    # is_user_in_group(sub_child_user, sub_child_user)  # we expect a ValueError to be thrown, String as Group
    # is_user_in_group(sub_child_user, None)  # we expect a ValueError to be thrown, None as Group
    # is_user_in_group(parent, parent)    # we expect a ValueError to be thrown, NonString as User
    # child.add_user("")  # we expect a ValueError to be thrown, Empty string as user name
    # child.add_group(None)   # we expect a ValueError to be thrown, None as group name


if __name__ == "__main__":
    main()
