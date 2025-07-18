# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

   
class Solution:
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True  # Both trees are empty
    
    if not p or not q:
        return False  # One tree is empty, the other is not
    
    if p.val != q.val:
        return False  # Values do not match
    
    # Recursively check left and right subtrees
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    
    
