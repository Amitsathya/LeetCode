# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def dfs(node, path):
            if not node:
                return
            # If it's a leaf node, add full path
            if not node.left and not node.right:
                res.append(path + str(node.val))
                return
            # Otherwise keep traversing
            dfs(node.left, path + str(node.val) + "->")
            dfs(node.right, path + str(node.val) + "->")

        dfs(root, "")
        return res


