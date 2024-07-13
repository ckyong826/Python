# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def transRight(root,lvl):
            if root:
                if len(res)==lvl:
                    res.append(root.val)
                transRight(root.right,lvl+1)
                transRight(root.left,lvl+1)
        res=[]
        transRight(root,0)
        return res