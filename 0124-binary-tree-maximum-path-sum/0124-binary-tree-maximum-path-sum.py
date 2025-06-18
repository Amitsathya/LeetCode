# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def bfs(root):
            if not root:
                return 0
            
            leftMax = max(bfs(root.left), 0)
            rightMax = max(bfs(root.right), 0)
            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)
        bfs(root)
        return res[0]
        