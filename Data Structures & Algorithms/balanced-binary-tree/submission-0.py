# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True

        def dfs(node):
            nonlocal isBalanced

            if not node:
                return -1

            leftHeight = 1 + dfs(node.left)
            rightHeight = 1 + dfs(node.right) 

            if abs(leftHeight - rightHeight) > 1:
                isBalanced = False

            return max(leftHeight, rightHeight)

        dfs(root)
        return isBalanced