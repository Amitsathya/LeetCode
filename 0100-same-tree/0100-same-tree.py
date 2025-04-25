# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            for _ in range(len(q1)):
                P = q1.popleft()
                Q = q2.popleft()

                if P is None and Q is None:
                    continue
                if P is None or Q is None or P.val != Q.val:
                    return False
                
                q1.append(P.left)
                q1.append(P.right)
                q2.append(Q.left)
                q2.append(Q.right)
        return True

            
        