# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# traverse arrays
# . 0   -3   -2   -1   0   1     2       3
#                      2
#  1              9       8

#  2.         4.       1        7

#  3.    3         11

from collections import defaultdict
from collections import deque

'''
    PLAN
        initialize vertical index to list of nodes 
        create helper functions to traverse tree in bft
            initilize queue
            initilaze the min_colum and max coloum to keep trck teh width of the tree
            add  root node zero as a tuple to inidicate vertical index and node  
            loop through queue
                take out first tuple and update vertical index to list of node map
                update min_column and max_column
                add left and right child to queue
                repeat this process till queue is empty
           loop through range function to create index for vertical index map 
            collect all the list and combine them in result     
'''


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        veritcal_index_to_nodes_map = defaultdict(list)
        queue = deque([(root, 0)])
        min_column = 0
        max_column = 0
        while queue:
            node, column = queue.popleft()
            if node:
                veritcal_index_to_nodes_map[column].append(node.val)
                min_column = min(min_column, column)
                max_column = max(max_column, column)
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))
        return [veritcal_index_to_nodes_map[index] for index in range(min_column, max_column + 1)]
