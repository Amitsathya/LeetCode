# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(p, root, q):
            if not root:
                return True
            if p < root.val < q:
                return isValid(p, root.left, root.val) and isValid(root.val, root.right, q)
            else:
                return False
        return isValid(float("-inf"), root, float('inf'))