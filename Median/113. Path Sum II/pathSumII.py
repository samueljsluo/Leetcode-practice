# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
#         if not root: return []
#         res = []
#         temp = []
#         self.helper(root, res, temp, targetSum)
#         return res
        
#     def helper(self, node, res, temp, targetSum):
#         if targetSum==node.val and not node.left and not node.right:
#             temp.append(node.val)
#             res.append(temp[:])
#             temp.pop()
#             return
        
#         if node.left:
#             temp.append(node.val)
#             targetSum-=node.val
#             self.helper(node.left, res, temp, targetSum)
#             targetSum+=node.val
#             temp.pop()
        
#         if node.right:
#             temp.append(node.val)
#             targetSum-=node.val
#             self.helper(node.right, res, temp, targetSum)
#             targetSum+=node.val
#             temp.pop()

        # improvement
        res = []
        self.dfs(root, res, [], targetSum)
        return res

    def dfs(self, node, res, temp, targetSum):
        if not node: return 
        if node.val==targetSum and not node.left and not node.right:
            res.append(temp+[node.val])
            return
        self.dfs(node.left, res, temp+[node.val], targetSum-node.val)
        self.dfs(node.right, res, temp+[node.val], targetSum-node.val)
        