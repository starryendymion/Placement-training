class Solution:
 def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
  answer = None
  def lowest_common_ancestor(root,a,b):
    nonlocal answer
    if not root:
        return None
    
    left_returned = lowest_common_ancestor(root.left,a,b)
    right_returned = lowest_common_ancestor(root.right,a,b)

    #Leaf CASE 
    if (root.left is None) and (root.right is None):
        if (root==a) or (root==b):
            return root 
        else:
            return None
        
    # Base Case
    if (left_returned==a and right_returned==b) or (left_returned==b and right_returned==a):
        if not answer:
            answer = root            
    
    # CASe if root is another element
    if (root==a) or (root==b):
        if (root==a) and ((left_returned==b) or (right_returned==b)):
            if not answer:
                answer=root
        elif (root==b) and ((left_returned==a) or (right_returned==a)):
            if not answer:
                answer=root

    if (left_returned==None) and (right_returned in (a,b)):
              return right_returned
    
    if (right_returned==None) and (left_returned in (a,b)):
              return left_returned
    
    if (left_returned is None) and (right_returned is None):
              if root in (a,b):
                 return root
              else:
                 return None 
  
  lowest_common_ancestor(root,p,q) 
  return answer