class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(n):
            for j in range(i+1, n+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[n]


print(Solution().wordBreak(s = "leetcode", wordDict = ["leet", "code"]))
print(Solution().wordBreak(s = "applepenapple", wordDict = ["apple", "pen"]))
print(Solution().wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))


