class Solution:
    def subarraySum(self, nums, k: int) -> int:
        he, ans = 0, 0
        mp = {0:1}
        for num in nums:
            he += num
            ans += mp.get(he - k, 0)
            mp.setdefault(he, 0)
            mp[he] += 1
        return ans

print(Solution().subarraySum(nums = [1,1,1], k = 2))