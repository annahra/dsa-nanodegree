Union and Intersection

Time Complexity:
Union:
The checks at the beginning of the function all run in 0(1) constant time.
We then interate through post of the linked lists so we that we can append it
to a new result list. If the size of linked list one is n and the size of linked
list two is m, then the time complexity of this algorithm is O(n+m), as we
traverse through both lists.
Intersection:
In this algorithm we traverse through both linked lists as well, so the time
complexity is O(n+m).

Space Complexity:
Union:
We return a list of size O(n+m), so that is the space complexity as well.
Intersection:
We create a set of size O(n), but we return a list that is the size of 
the union of LinkedList 1 and 2. In the worst case, each value in LinkedList 1
is also in LinkedList 2. So we can deduce that the worst case space complexity
is O(n).