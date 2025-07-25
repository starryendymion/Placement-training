# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []

        def dfs(root):
            nonlocal inorder
            if not root:
                return 0
            dfs(root.left)
            inorder.append(root.val)
            dfs(root.right)

        dfs(root)
        return inorder