class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        count = [[] for i in range(len(nums) + 1)]
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        for key, value in freq.items():
            count[value].append(key)
        res = []
        for i in range(len(count) -1, -1, -1):
            for n in count[i]:
                res.append(n)
                if len(res) == k:
                    return res
