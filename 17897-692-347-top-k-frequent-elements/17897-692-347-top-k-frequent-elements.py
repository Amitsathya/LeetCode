class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        count = [[] for i in range(len(nums) + 1)]
        for n in nums:
            freq[n] = freq.get(n,0)+1
        for i, n in freq.items():
            count[n].append(i)
        res = []
        for i in range(len(nums),0, -1):
            for v in count[i]:
                res.append(v)
                if len(res) == k:
                    return res

            
        