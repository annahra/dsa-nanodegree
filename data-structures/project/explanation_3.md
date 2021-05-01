Huffman Coding

Time Complexity:
There are two main operations happening - the encoding of data and the decoding of data.
Encoding:
We first iterate through the length of the input, n, and create a frequency map. 
We then iterate n times once more by creating nodes out of the frequency map. 
We then create a min heap using the heapq library; pushing items onto the heap takes 
O(nlog n). We then create the Huffman tree - this means we traverse a condensed length of the
list. Since n is bigger than this length, we can ignore this term. We then find the codes
associated with this list, which takes the same amount of time as the traversal of
the list. We then iterate through n once more to encode the data. This means that the
time complexity of the encoding function will be O(n + nlog n). 
Decoding: 
We iterate through the condensed version of n, let's call this m. We also iterate through
the tree. This makes this time complexity O(m + log n)

Space Complexity:
Encoding:
Creating the frequency map would create O(m) space complexity, where m is the number of keys
in the frequency map. Creating the nodes would take O(4m) space (because the nodes have 
4 fields). Creating the minheap would be another O(m) space. The recursive call would be
O(m) space as it does the recursion as well. So we can deduce that encoding would take
O(m) space.
Decoding:
Decoding the message would take O(j) space where j is the size of the encoded message.