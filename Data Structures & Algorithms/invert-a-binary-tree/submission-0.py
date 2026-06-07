# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recursiveTraverse(node):
            if not node:
                return
            
            recursiveTraverse(node.left)
            recursiveTraverse(node.right)

            node.left, node.right = node.right, node.left

        recursiveTraverse(root)

        return root