# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
    if we can print the right most elmement at each level than
        we can simply reduce this problem to BFT

    initialize queue with root
        iterate queue till we have elements
            - iterate the current length of the queue
            - pop child and keep checking if it's last child
            - add left or right child back to queue

    process all the nodes at each level and store it's last element to the reuslt array
    return the result


'''
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
