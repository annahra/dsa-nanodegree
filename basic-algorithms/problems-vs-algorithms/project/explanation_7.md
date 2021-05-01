HTTP Router with Tries

Space Complexity (Data Structure):
We are using a Trie, therefore the worse cast space complexity of the Trie will be O(n*m) 
where n is the number of web links inputed in the Trie, and m is the link with the longest 
number of directories in its path. This represents the number of TrieNodes that will be made.
The class that wraps the Tries doesn't add any significant space complexity as it is just
a wrapper class


Time Complexity:
Since we are only searching for one path, that path will travel along only one branch
of the Trie. So time time complexity for both inserting a link and searching for a link
is O(m) where m is the link with the largest amount of directories in its path. We
iterate through m when we iterate through the array that was constructed when we split
the path link string by forward slashes.