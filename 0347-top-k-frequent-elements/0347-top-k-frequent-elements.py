class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for i, v in count.items():
            freq[v].append(i)
        res = []
        for i in range(len(nums), -1, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k :
                    return res
        return -1

        