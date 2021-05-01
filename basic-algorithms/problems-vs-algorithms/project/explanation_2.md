Search in a Rotated Sorted Array

Data Structure Choice:
The problem necessitated that the input would be an array. No other data structures were
used. This makes space complexity O(1) constant space.

Time Complexity:
We do a different version of the binary search, except now we must check if the target
number is in a particular half of the array. These checks take O(1) constant time, so 
therefore the overall complexity of the algorithm is O(logn) time.