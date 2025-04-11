# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
    base case:
    if root is None:
        return None

    if root==p or root==q:
        return root
    if left and right than return root
    return left or right

    lowestCommonAncestor(root) =root or lowestCommonAncestor(root.left) or lowestCommonAncestor(root.left)

'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left is not None else right

