class TreeNode:
    def __init__(self, val=0, left=None, right=None, depth=0):
        self.val = val
        self.left = left
        self.right = right
        self.depth = 0
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
     if not root:
           return 0

     root.depth= 1
     max_depth = 1
     

     stack = [root]
    
     while stack:
        node = stack.pop()
        if node.depth > max_depth:
            max_depth = node.depth
        # Add children to stack if they exist
        if node.left:
            stack.append(node.left)
            node.left.depth = node.depth + 1 

        if node.right:
            stack.append(node.right)
            node.right.depth = node.depth + 1 

     return max_depth