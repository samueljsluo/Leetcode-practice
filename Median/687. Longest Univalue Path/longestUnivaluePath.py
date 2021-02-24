# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root: return 0
        res = [0]
        self.helper(root, res)
        return res[0]
    
    def helper(self, node, res):
        if not node: return 0
        left = self.helper(node.left, res)
        right = self.helper(node.right, res)
        pl = 0
        pr = 0
        if node.left and node.val == node.left.val: pl = left + 1
        if node.right and node.val == node.right.val: pr = right + 1
        res[0] = max(res[0], pl+pr)
        return max(pl, pr)
        