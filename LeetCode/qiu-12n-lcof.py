class Solution:
    def di(self, n):
        self.ans |= n
        n and self.di(n-1)

    def sumNums(self, n: int) -> int:
        self.ans = 0
        self.di(n)
        return self.ans

print(Solution().sumNums(3))
print(Solution().sumNums(9))