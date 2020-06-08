class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        dp = [1]*(len(num)+1)
        for i in range(1, len(num)):
            dp[i+1] = dp[i]
            if int(num[i-1:i+1]) < 26 and int(num[i-1]):
                dp[i+1] += dp[i-1]
        return dp[-1]

print(Solution().translateNum(12258))
print(Solution().translateNum(506))