# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            new_root = TreeNode()
            if root.left and root.right:
                parent = root
                new_root = root.right
                while new_root.left:
                    parent = new_root
                    new_root = new_root.left
                
                if parent != root:  # if there are more than one child on the right side
                    parent.left = new_root.right
                    new_root.right = root.right  # if this line out side of if function there would be circle in TreeNode
                new_root.left = root.left
                
                del root
                return new_root
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
        return root
