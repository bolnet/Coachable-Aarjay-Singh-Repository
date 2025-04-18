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
from collections import defaultdict


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
'''
Single Pass
if we can print the right most value at each level
    than this problem can be reduce to trivial BFT.
    BFT to travel the tree
        - map level to nodes
    build result from map
'''


def rightSideView_single_pass(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    queue = deque([(root, 0)])
    result = []
    level_to_node_map = defaultdict(list)
    visited = set()
    visited.add(root)
    while queue:
        node, level = queue.popleft()
        level_to_node_map[level].append(node.val)
        if node.left and node.left not in visited:
            queue.append((node.left, level + 1))
            visited.add(node.left)
        if node.right and node.right not in visited:
            queue.append((node.right, level + 1))
            visited.add(node.right)
    for level, list_of_nodes in level_to_node_map.items():
        result.append(list_of_nodes[-1])
    return result
