class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = set()
        for n in nums:
            if n not in res:
                res.add(n)
            else:
                return True
        return False
        