"""
Problem 1: LRU Cache
Author: Annah Ramones

Version Date: March 15, 2021

Test Case 3 is commented out as we expect each case in
Test Case 3 to raise an Exception.
"""

import sys


class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        return

    def remove_LRU(self):
        if self.head is None:
            return

        if not self.head.next:
            removed_key = self.head.key
            self.head = None
            self.tail = None
            return removed_key

        removed_key = self.head.key
        self.head.next.prev = None
        self.head = self.head.next
        return removed_key

    def move_MRU(self, node):
        # before calling this function, you must know that the value is for sure in the list
        if self.tail == node:
            return

        # special case where node to be moved is the head
        if self.head == node:
            self.tail.next = self.head
            self.head.next.prev = None
            next_node = self.head.next
            self.head.next = None
            self.head.prev = self.tail
            self.tail = self.head
            self.head = next_node
            return

        self.tail.next = node
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.tail
        node.next = None
        self.tail = node
        return

    def __repr__(self):
        node = self.head
        print('current list: ')
        while node:
            print(node.key)
            node = node.next
        print('done with current list')


class LRUCache(object):

    def __init__(self, max_capacity):
        # Initialize class variables
        if type(max_capacity) is not int or max_capacity <= 0:
            raise Exception("Not a valid list capacity")

        if max_capacity > sys.maxsize / 5:
            raise Exception("Cache Capacity too big, choose a smaller number")

        self.max_capacity = max_capacity
        self.dlinked_list = DoublyLinkedList()
        self.dict = {}

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.dict:
            return -1
        self.dlinked_list.move_MRU(self.dict.get(key)[1])
        return self.dict.get(key)[0]

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        node = Node(key)

        if len(self.dict) < self.max_capacity:
            if key in self.dict:
                self.dlinked_list.move_MRU(self.dict.get(key)[1])
                self.dict[key] = [value, self.dict.get(key)[1]]
            else:
                self.dlinked_list.append(node)
                self.dict[key] = [value, node]

        elif len(self.dict) == self.max_capacity:
            if key in self.dict:
                self.dlinked_list.move_MRU(self.dict.get(key)[1])
                self.dict[key] = [value, self.dict.get(key)[1]]
            else:
                removed_key = self.dlinked_list.remove_LRU()
                del self.dict[removed_key]
                self.dlinked_list.append(node)
                self.dict[key] = [value, node]


def main():
    # Test Case 1
    print("Test Case 1 - Basic Function")
    our_cache = LRUCache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    print('Should return 1: ', our_cache.get(1))  # returns 1
    print('Should return 2: ', our_cache.get(2))  # returns 2
    print('Should return -1: ', our_cache.get(9))  # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    print('Should return -1: ', our_cache.get(
        3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    print('End of Test Case 1\n')

    # Test Case 2
    print("Test Case 2 - Small Cache, None Key Value")
    new_cache = LRUCache(2)

    new_cache.set('a', None)
    new_cache.set(None, 22)

    print('Should return 22: ', new_cache.get(None))  # returns 22

    new_cache.set(None, 102)

    print('Should return None: ', new_cache.get('a'))  # returns None doesnt put another None in doubly link list)
    print('Should return 102: ', new_cache.get(None))  # returns 102

    new_cache.set(3, 33)
    print('Should return -1: ', new_cache.get('a'))  # returns -1
    print('End of Test Case 2\n')

    # Test Case 3
    print("Test Case 3 - Invalid size of cache, uncomment cases")
    # zero_cache = LRUCache(0)    # throws exception
    # str_cache = LRUCache('a')   # throws exception
    # neg_cache = LRUCache(-1)    # throws exception
    # none_cache = LRUCache(None)   # throws exception
    # high_capacity = LRUCache(sys.maxsize)    # throws exception "Cache Capacity too big, choose a smaller number"
    print('End of Test Case 3\n')

    # Test Case 4
    print("Test Case 4 - LRU Cache of size 1")
    a_cache = LRUCache(1)
    a_cache.set(1, 1)
    print('Should return 1: ', a_cache.get(1))
    a_cache.set(2, 2)
    print('Should return 2: ', a_cache.get(2))
    a_cache.set(3, 3)
    a_cache.set(4, 4)
    print('Should return 4: ', a_cache.get(4))


if __name__ == "__main__":
    main()
