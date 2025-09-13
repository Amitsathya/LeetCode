class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        counts1, counts2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            counts1[ord(s1[i]) - ord('a')] += 1
            counts2[ord(s2[i]) - ord('a')] += 1
        l, matches = 0, 0
        for i in range(26):
            matches += 1 if counts1[i] == counts2[i] else 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            c = ord(s2[r]) - ord('a')
            counts2[c] += 1
            if counts1[c] == counts2[c]:
                matches += 1
            elif counts1[c] + 1 == counts2[c]:
                matches -= 1
            c = ord(s2[l]) - ord('a')
            counts2[c] -= 1
            if counts1[c] == counts2[c]:
                matches += 1
            elif counts1[c] - 1 == counts2[c]:
                matches -= 1
            l += 1
        return matches == 26
