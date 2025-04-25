# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
                P, Q = stack.pop()

                if P is None and Q is None:
                    continue
                if P is None or Q is None or P.val != Q.val:
                    return False
                
                stack.append([P.left, Q.left])
                stack.append([P.right, Q.right])
        return True

            
        