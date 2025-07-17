# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(left, root, right):
            if not root: return True

            if not (left < root.val < right):
                return False
            
            return isValid(left, root.left, root.val) and isValid(root.val, root.right, right)
        return isValid(float("-inf"), root, float("inf"))
        