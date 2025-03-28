# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    # traverse arrays
        #. 0   -3   -2   -1   0   1     2       3
        #                      2
        #  1              9       8

        #  2.         4.       1        7

        #  3.    3         11


        # if we assume root at 0th column than left child will be on -1 column and right child will be in 1 column
        # we can traverse tree using BFS to build dictionary which can record nodes belong to each coloumn
from collections import defaultdict
from collections import deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d=defaultdict(list)
        queue=deque([(root,0)])
        while queue:
            node,column=queue.popleft()
            if node:
                d[column].append(node.val)
                queue.append((node.left,column-1))
                queue.append((node.right,column+1))
        return [d[x ]for x in sorted(d.keys())]





