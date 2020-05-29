class Solution:
    def rob(self, nums) -> int:
        ans = 0
        dp = [0] * (len(nums)+5)
        for i in range(len(nums)):
            dp[i+2] = max(dp[i]+nums[i], dp[i+1])
            ans = max(ans, dp[i+2])
        return ans

print(Solution().rob([1,2,3,1]))
print(Solution().rob([2,7,9,3,1]))