class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            w = [0] * 26
            for c in s:
                w[ord(c) - ord('a')] += 1
            res[tuple(w)].append(s)
        return list(res.values())