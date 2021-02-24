# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        #     1
        #    / \
        #   2   3
        #  / \
        # 4   4
        # max is 4-2-4 or 4-2-1-3
        # we update answer in each treverse, which cosider both side of children(4-2-4)
        # when return, only consider larger side, since we can not return 4-2-4
        
        if not root: return 0
        res = [float('-inf')] # pass by reference
        self.helper(root, res)
        return res[0]
        
    def helper(self, root, res):
        if not root: return 0
        left = max(0, self.helper(root.left, res))
        right = max(0, self.helper(root.right, res))
        res[0] = max(res[0], left + right + root.val)  # update maximum, here consider both side since the maximum may happen in local
        return max(right, left) + root.val # when return, only consider one side(left or right)
        