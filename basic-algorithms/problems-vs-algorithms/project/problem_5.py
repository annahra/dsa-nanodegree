"""
Problem 5: Autocomplete with Tries (Suffixes)

Version Date: April 12, 2021
"""


class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        # Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point
        result_list = []

        for letter, c_node in self.children.items():
            if c_node.is_word:
                result_list.append(suffix + letter)

            if len(c_node.children) > 0:
                result_list.extend(c_node.suffixes(suffix + letter))

        return result_list


class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        node = self.root
        for char in word:
            node.insert(char)
            node = node.children[char]
        node.is_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

def main():
    MyTrie = Trie()
    wordList = [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
    ]
    for word in wordList:
        MyTrie.insert(word)

    def f(prefix):
        if prefix != '':
            prefixNode = MyTrie.find(prefix)
            if prefixNode:
                print('\n'.join(prefixNode.suffixes()))
            else:
                print(prefix + " not found")
        else:
            print('')

    # Test Case 1 - Basic Function
    print("Test Case 1 - Basic Function")
    print("Prefix: ant, Suffixes:")
    f("ant")
    print("\nPrefix: tr, Suffixes:")
    f("tr")
    print("\nPrefix: trip, Suffixes:")
    f("trip")
    print("\nPrefix: fa, Suffixes:")
    f("fa")
    print("\nPrefix: f, Suffixes:")
    f("f")
    print("End of Test Case 1\n")

    # Test Case 2 - Entire word as input
    print("Test Case 2 - Entire word as input")
    print("Prefix: trie, Suffixes: (we expect nothing)")
    f("trie")
    print("Prefix: factory, Suffixes: (we expect nothing)")
    f("factory")
    print("End of Test Case 2\n")

    # Test Case 3 - Empty String
    print("Test Case 3 - Empty String (expect nothing)")
    f("")
    print("End of Test Case 3\n")


if __name__ == '__main__':
    main()
