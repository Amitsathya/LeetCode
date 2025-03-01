class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for w in strs:
            count = [0] *26
            for c in w:
                count[ord(c) - ord('a')] += 1
            freq[tuple(count)].append(w)
        return list(freq.values())
                
        