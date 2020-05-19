class Solution:
    def judge(self, s: str, l: int, r: int, mark: bool) -> bool:
        while l < r:
            if s[l] != s[r]:
                if mark:
                    return self.judge(s, l, r-1, False) or self.judge(s, l+1, r, False)
                else:
                    return False
            l += 1
            r -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        return self.judge(s, 0, len(s)-1, True)


print(Solution().validPalindrome('abca'))
