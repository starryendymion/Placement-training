class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
     if not root:
        return

     stack = [root]

     while stack:
        node = stack.pop()   # Swap left and right
        node.left, node.right = node.right, node.left
        # Add children to stack if they exist
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
     return root