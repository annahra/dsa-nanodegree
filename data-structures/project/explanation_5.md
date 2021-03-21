BlockChain

Time Complexity:
I've chosen to implement the blockchain with a linked list because block chains
are primarily for book keeping, so there was no need to use a tree or stack or queue.
Appending to the linked list takes O(1) constant time because I have a pointer to the
tail node. Traversing through the linked list takes O(n) linear time where n is the 
number of blocks in the blockchain.

Space Complexity:
For each block in the blockchain, we save 4 fields of data: data, previous hash, hash,
and the next pointer. So this makes our space complexity O(4n). However, we can 
simplify it to O(n).