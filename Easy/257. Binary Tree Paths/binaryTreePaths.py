# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode):
        # Solution 1:
        if not root: return []
        res = []
        temp = []
        self.helper(root, res, temp)
        return res
        
    def helper(self, node, res, temp):
        if not node.left and not node.right:
            res.append('->'.join([str(x) for x in temp+[node.val]]))
            return
        if node.left:
            self.helper(node.left, res, temp+[node.val])
        if node.right:
            self.helper(node.right, res, temp+[node.val])
        
        # Solution 2:
        # if not root: return []
        # res = [str(root.val) + '->' + node for node in self.binaryTreePaths(root.left)]
        # res+= [str(root.val) + '->' + node for node in self.binaryTreePaths(root.right)]
        # return res or [str(root.val)] # if there is no children return its value