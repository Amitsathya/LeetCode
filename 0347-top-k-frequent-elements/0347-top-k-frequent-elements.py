class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        count = [[] for i in range(len(nums) +  1)]
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        for i, v in freq.items():
            count[v].append(i)
        res = []
        for i in range(len(nums), -1, -1):
            for j in count[i]:
                res.append(j)
                if len(res) == k:
                    return res
        