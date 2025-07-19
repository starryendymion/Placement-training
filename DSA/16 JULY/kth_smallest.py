class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
     ans = None
     def sol(root):
         nonlocal ans
         nonlocal k
         if not root:
             return 
         sol(root.left)
         if k==1:
            ans = root.val
            k=0
         elif k>1:
            k-=1
         sol(root.right)
     sol(root)
     return ans   