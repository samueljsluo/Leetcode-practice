# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def solution1():
            def helper(root, res, level):
                if not root:
                    return

                if level >= len(res):
                    res.append([])
                res[level].append(root.val)
                if root.left:
                    helper(root.left, res, level+1)
                if root.right:
                    helper(root.right, res, level+1)
                return sum(res[-1])
            
            res = [[]]
            level = 0
            return helper(root, res, level)
        
        def solution2():
            queue = deque()
            queue.append((root, 0))  # node, depth
            mx_depth = 0
            res = 0
            while queue:
                node, depth = queue.popleft()
                if mx_depth < depth:
                    mx_depth = depth
                    res = 0  # there is node deeper than current. so reset the result
                if mx_depth == depth:
                    res+=node.val
                if node.right: 
                    queue.append((node.right, depth+1))
                if node.left:
                    queue.append((node.left, depth+1))
            return res
                    
        return solution2()