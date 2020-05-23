from collections import Counter, defaultdict
class Solution:

    def judge(self) -> bool:
        """
            判断是否,符合
        """
        for k in self.target:
            if self.target[k] > self.count[k]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        ans, anslen = '', len(s)+1
        self.target = Counter(t)
        # print(self.target)
        self.count = defaultdict(int)
        # 设置滑动窗口的两端
        l, r = 0, 0
        for i in s:
            self.count[i] += 1
            # print(self.count)
            r += 1
            # 试探性的缩小左端
            while l < r and self.judge():
                self.count[s[l]] -= 1
                if r - l < anslen:
                    ans = s[l:r]
                    anslen = r - l
                l += 1
        return ans

print(Solution().minWindow("ADOBECODEBANC", "ABC"))