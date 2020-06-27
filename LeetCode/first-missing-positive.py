class Solution:
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)
        mark = [0] * (n+2)
        for i in nums:
            if i >= 1 and i <= n:
                mark[i] = 1
        for i in range(1, n+2):
            if mark[i] == 0:
                return i


print(Solution().firstMissingPositive([1,2,0]))
print(Solution().firstMissingPositive([1,2,3]))
print(Solution().firstMissingPositive([3,4,-1,1]))
print(Solution().firstMissingPositive([7,8,9,11,12]))