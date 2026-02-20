class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backTrack(i, total, curr):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            curr.append(candidates[i])
            backTrack(i, total + candidates[i], curr)
            curr.pop()
            backTrack(i + 1, total, curr)
        backTrack(0, 0, [])
        return res