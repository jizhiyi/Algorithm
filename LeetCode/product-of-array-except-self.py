class Solution:
    def productExceptSelf(self, nums):
        nums = [1] + nums + [1]
        ans = [i for i in nums]
        n = len(nums)
        for i in range(1, n-1):
            ans[i] *= ans[i-1]
            nums[n-i-1] *= nums[n-i]
        now, pre = 1, 1       
        for i in range(1, n-1):
            now = ans[i]
            ans[i] = pre * nums[i+1]
            pre = now
        return ans[1:n-1]


print(Solution().productExceptSelf([1,2,3,4]))