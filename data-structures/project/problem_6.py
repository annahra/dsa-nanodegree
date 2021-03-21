"""
Problem 6: Union and Intersection
Author: Annah Ramones

Version Date: March 19, 2021

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def to_list(llist):
    result = list()
    node = llist.head
    while node:
        result.append(node.value)
        node = node.next
    return result


def union(llist_1, llist_2):
    if llist_1.head is None and llist_2.head is not None:
        return to_list(llist_2)
    elif llist_2.head is None and llist_1.head is not None:
        return to_list(llist_1)
    elif llist_1.head is None and llist_2.head is None:
        return list()

    result = to_list(llist_1)
    result.extend(to_list(llist_2))

    return result


def intersection(llist_1, llist_2):
    if llist_1.head is None or llist_2.head is None:
        return list()

    lset = set()
    result = list()

    node1 = llist_1.head
    while node1:
        if node1.value not in lset:
            lset.add(node1.value)
        node1 = node1.next

    node2 = llist_2.head
    while node2:
        if node2.value in lset:
            result.append(node2.value)
        node2 = node2.next

    return result


def main():
    # Test case 1 - Intersection between lists
    print("Test Case 1 - Intersection between lists")
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))
    print('End of Test Case 1\n')

    # Test case 2 - No Intersection between lists
    print("Test Case 2 - No Intersection between lists")
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))
    print(intersection(linked_list_3, linked_list_4))
    print('End of Test Case 2\n')

    print("Test Case 3 - Empty Lists")
    llist_5 = LinkedList()
    llist_6 = LinkedList()
    print('Union of empty lists:', union(llist_5, llist_6))
    print('Intersection of empty lists:', intersection(llist_5, llist_6))

    llist_7 = LinkedList()
    llist_8 = LinkedList()

    element_1 = [1, 7, 8, 9, 11, 21, 1]
    for i in element_1:
        llist_7.append(i)

    print('Union of list 1 with empty list:', union(llist_7, llist_8))
    print('Intersection of list 1 with empty list:', intersection(llist_7, llist_8))

    llist_9 = LinkedList()
    llist_10 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    for i in element_1:
        llist_10.append(i)

    print('Union of list 2 with empty list:', union(llist_9, llist_10))
    print('Intersection of list 2 with empty list:', intersection(llist_9, llist_10))
    print('End of Test Case 3\n')


if __name__ == '__main__':
    main()
