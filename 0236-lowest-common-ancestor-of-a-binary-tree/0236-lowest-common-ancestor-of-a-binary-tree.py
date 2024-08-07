# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def inOrder(root,p,q):
            if not root or root.val==p.val or root.val == q.val:
                return root
            left=inOrder(root.left,p,q)
            right=inOrder(root.right,p,q)
            if left and right:
                return root
            return left if left else right
        return inOrder(root,p,q)
