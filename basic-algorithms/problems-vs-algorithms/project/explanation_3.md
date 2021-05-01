Rearrange Array Elements

Space Complexity:
We are using the mergesort algorithm to sort a list. The space complexity of this is 
O(logn) because lists use pointers (as opposed to recopying the whole array). However
because of Auxillary Space, the space complexity is O(n).

Time Complexity:
The time complexity of the merge sort algorithm is O(nlogn). The time complexity
of iterating through the sorted array is O(n). Therefore the time complexity is 
O(n + nlogn), but this reduces to O(nlogn).