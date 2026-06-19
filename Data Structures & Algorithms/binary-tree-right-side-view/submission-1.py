# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque()
        q.append(root)

        view = []
        while q:
            print(q)
            level_size = len(q)
            
            print(level_size)
            for _ in range(level_size - 1):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            view_node = q.popleft()                
            view.append(view_node.val)
            if view_node.left:
                q.append(view_node.left)
            if view_node.right:
                q.append(view_node.right)

        return view
            