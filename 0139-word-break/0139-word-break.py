class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            if not dp[i]:
                continue
            
            for w in wordDict:
                if len(w) + i <= len(s) and s[i:i + len(w)] in wordDict:
                    dp[len(w) + i] = True
        return dp[len(s)]