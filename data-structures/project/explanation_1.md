LRU Cache

Data Structure Choice:
I needed the get and set methods of the LRUCache to be O(1) constant time.
Because of this, I chose to use a Hash Table, or Python Dictionary to set and retrieve
key-value pairs. This data structure does not properly address the prioritizing of 
recently used values. Because of this issue, I chose to use a Doubly Linked List. I chose
the head of the list to be the Least Recently Used item and the tail of the list
to be the Most Recently Used item. I used a Doubly Linked List instead of a Singly
Linked List so that I could move nodes to the tail in constant time. 

Time Complexity:
Get:
Getting items from the dictionary takes O(1) constant time. Moving the key node
to the tail of the Doubly Linked List takes O(1) constant time because we don't need
to iterate through the list to find the previous node. 
Set:
Setting a dictionary's key value pair takes O(1) constant time. Moving the key node
to the tail of the Doubly Linked List takes O(1) constant time. Appending a new key
node to the tail of the list takes O(1) constant time as well. 

Space Complexity:
For each key-value pair, we need to keep a node, as well as an entry in the dictionary.
The value will be a list of the value in the first index and the Node in the second index.
We need to keep a key variable, next reference and previous reference for every node.
So for n, where n is the maxiumum size of the cache, the space complexity is O(5n) (the
items needed for the node and the 2 list items in the value of the key-value pair. 
This can be reduced to O(n)