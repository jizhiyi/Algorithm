from collections import defaultdict
class Solution:
    def findf(self, x):
        if self.father[x] != x:
            self.father[x] = self.findf(self.father[x])
        return self.father[x]


    def join(self, a, b):
        af = self.findf(a)
        bf = self.findf(b)
        if af != bf:
            self.father[af] = bf
            self.count[bf] += self.count[af]



    def longestConsecutive(self, nums) -> int:
        self.father = dict()
        self.count = defaultdict(lambda : 1)
        ans = 0
        for i in nums:
            if i not in self.father:
                self.father[i] = i
            for j in range(-1, 2, 2):
                if i+j in self.father:
                    self.join(i, i+j)
            ans = max(ans, self.count[self.findf(i)])
        return ans


        



print(Solution().longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))