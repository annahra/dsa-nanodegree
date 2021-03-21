File Recursion

Time Complexity:
We know that the time complexity of a recursive function is O(numBraches^(depth)). 
In our problem, for the worst case, the number of branches would be the maximum number 
of items at a level. Let's call this number f. To illustrate this with our 
current example, "./testdir", the number of branches would be 7 since is the maximum
number of items is at the level "./testdir/" (subdir1, subdir2, subdir3, subdir4, 
subdir5, t1.c, t1.h). This is the maximum number of items that our for loop with loop through.
The depth of our tree would be the maximum depth of the nexted folders, lets 
call this d. For example, the maximum depth for "./testdir" is 3, given 
by the path "./testdir/subdir3/subsubdir1". So the time complexity would be
O(f^d). 

Space Complexity:
The space complexity is O(n) where n is the total number of folders to call the recursive
function on. Athough there will be (at maximum) O(f^d) nodes in the recursive tree,
only O(n) would exist at one time. 