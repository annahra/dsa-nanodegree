Active Directory

Time Complexity:
We know that the time complexity of a recursive function is O(numBraches^(depth)).
For the worst case of this problem, the number of branches would be the maximum
number of groups + users on a certain level. This is because we have to iterate
through the maximum number of groups + users at each depth (worst case). The depth
for this problem would be the number of directories to traverse. This is different
at each level of the Active Directory Tree. For example, if the group we were interested
in was the Parent group, we'd have to traverse through Child and Sub Child, giving us a depth
of 3. However, if we were interested in Sub Child, we would only have a depth of 1. 
So the time complexity would be O((g+u)^d), where g is the number of groups below 
a certain directory, u is the number of users below the same directory, and d is the 
number of levels below the same directory. 

Space Complexity:
The space complexity is O(d) which is essentially the space that the call stack takes.  