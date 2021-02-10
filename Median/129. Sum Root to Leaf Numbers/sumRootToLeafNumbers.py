# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # Solution 1:
#         res = []
#         temp = ''
#         self.helper(root, res, temp)
#         return sum(res)
    
#     def helper(self, node, res, temp):
#         if not node: return
#         if not node.left and not node.right:
#             temp+=str(node.val)
#             res.append(int(temp))
#         self.helper(node.left, res, temp+str(node.val))
#         self.helper(node.right, res, temp+str(node.val))

        
        # Solution 2:
        #       1
        #      / \
        #     2   3
        # treverse to next level
        #       1
        #      / \
        # 1*10+2  3+1*10
        #
        # return left node val + right node val
        if not root: return 0
        if not root.left and not root.right:
            return root.val
        if root.left:
            root.left.val+=root.val*10
        if root.right:
            root.right.val+=root.val*10
        return self.sumNumbers(root.left) + self.sumNumbers(root.right)