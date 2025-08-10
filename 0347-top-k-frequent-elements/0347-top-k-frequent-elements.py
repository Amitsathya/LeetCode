class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums) + 1)]
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        for i, v in freq.items():
            count[v].append(i)
        res = []
        for i in range(len(count) - 1, -1, -1):
            for v in count[i]:
                res.append(v)
                if len(res) == k:
                    return res
        