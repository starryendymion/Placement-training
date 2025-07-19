class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
      current_sum = 0
      flag = False
      path_len = -1

      if (root is not None) and (root.left is None) and (root.right is None) and (root.val==targetSum):
        return True

      def dfs(root,targetSum):
        nonlocal current_sum
        nonlocal flag
        nonlocal path_len

        if not root:
            return False
        
        if flag is not True:
            
         current_sum += root.val
         path_len += 1 
         if current_sum == targetSum:
           if path_len > 0 and (root.left is None) and (root.right is None):
            flag = True
         dfs(root.left,targetSum)
         dfs(root.right,targetSum)
         current_sum -= root.val
         path_len -= 1 

      dfs(root,targetSum)
      return flag 
    

