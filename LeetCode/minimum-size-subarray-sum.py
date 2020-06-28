class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        if s > sum(nums):
            return 0
        l = he = 0
        ans = n = len(nums)
        for r in range(n):
            he += nums[r]
            while he >= s:
                ans = min(r-l+1, ans)
                he -= nums[l]
                l+=1
        return ans



print(Solution().minSubArrayLen(s = 7, nums = [2,3,1,2,4,3]))
print(Solution().minSubArrayLen(s = 3, nums = [1, 1]))