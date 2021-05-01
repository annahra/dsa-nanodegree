Autocomplete with Tries

Space Complexity (Data Structure):
We are using a Trie, therefore the worse cast space complexity of the Trie will be O(n*m) 
where n is the number of words inputed in the Trie, and m is the word with the largest
amount of characters. This represents the number of TrieNodes that will be made.

Space Complexity (Algorithm):
Since we are recursively searching for a word in the Trie, the space complexity of our
algorithm will only need to account the recursive call stack. For the word with 
the most characters, that space will be O(m).

Time Complexity:
Since we are only searching for suffixes with the same prefix, we will not have to traverse
the entire Trie. In the worse case scenario, every word in the trie shares the same
suffix, therefore we will have to traverse the whole Trie. The time complexity in this case
is O(n*m) where n is the number of words inputted in the Trie and m is the length of the
longest word.