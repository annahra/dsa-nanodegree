"""
Problem 3: Huffman Coding

Author: Annah Ramones

Version Date: March 22, 2021

Basic Structure of code given by mentor on the helpdesk to get me started, and understanding
this problem.
MinHeap wrapper that allows us to sort the heap based on the key of an object
was taken from https://stackoverflow.com/questions/28016944/does-python-have-a-built-in-min-heap-data-structure

"""

import sys
import heapq


class MinHeap(object):
    def __init__(self, key, data=()):
        self.key = key
        self.heap = [(self.key(d), d) for d in data]
        heapq.heapify(self.heap)

    def push(self, item):
        decorated = self.key(item), item
        heapq.heappush(self.heap, decorated)

    def pop(self):
        decorated = heapq.heappop(self.heap)
        return decorated[1]

    def __len__(self):
        return len(self.heap)


class Node:
    def __init__(self, freq, char=None):
        self.freq = freq
        self.char = char
        self.left_child = None
        self.right_child = None

    def __lt__(self, other):
        return self.freq < other.freq


def merge_nodes(node1, node2):
    node = Node(node1.freq + node2.freq)
    node.left_child = node1
    node.right_child = node2
    return node


def get_codes_helper(node, value):
    codes = {}

    if node is None:
        return {}

    if node.char is not None:
        codes[node.char] = value

    codes.update(get_codes_helper(node.left_child, value + "0"))
    codes.update(get_codes_helper(node.right_child, value + "1"))

    return codes


def get_codes(tree):
    if tree.left_child is None and tree.right_child is None:
        return {tree.char: '0'}
    return get_codes_helper(tree, "")


def huffman_encoding(data):
    if data == "":
        return "", None

    char_freq = {}

    for char in data:
        char_freq[char] = char_freq.get(char, 0) + 1

    node_list = []

    for key in char_freq:
        node_list.append(Node(char_freq[key], key))

    min_heap = MinHeap(key=lambda node: node.freq, data=node_list)

    while min_heap.__len__() > 1:
        node1 = min_heap.pop()
        node2 = min_heap.pop()
        parent_node = merge_nodes(node1, node2)
        min_heap.push(parent_node)

    root = min_heap.pop()
    codes = get_codes(root)

    encoded_data = ""

    for char in data:
        encoded_data += codes[char]

    return encoded_data, root


def huffman_decoding(data,tree):
    if data == "":
        return ""

    message = ""

    curr_node = tree

    for character in data:
        if character == "0" and curr_node.left_child is None:
            message += curr_node.char
            continue
        elif character == "0":
            curr_node = curr_node.left_child
        else:
            curr_node = curr_node.right_child
        if curr_node.char is not None:
            message += curr_node.char
            curr_node = tree

    return message


if __name__ == "__main__":
    # Test Case 1: Basic Function
    print("Test Case 1 - Basic Function")
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}".format(decoded_data))
    print('End of Test Case 1\n')

    # Test Case 2: Empty String
    print("Test Case 2 - Empty String")
    empty_string = ""

    print("The size of the data is: {}".format(sys.getsizeof(empty_string)))
    print("The content of the data is: {}\n".format(empty_string))

    encoded_data, tree = huffman_encoding(empty_string)

    # print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}".format(decoded_data))
    print('End of Test Case 2\n')

    # Test Case 3: Similar Letter
    print("Test Case 3 - Similar Letter")
    same_letters = "aaaa"

    print("The size of the data is: {}".format(sys.getsizeof(same_letters)))
    print("The content of the data is: {}\n".format(same_letters))

    encoded_data, tree = huffman_encoding(same_letters)

    print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}".format(decoded_data))
    print('End of Test Case 3\n')
