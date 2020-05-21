class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = s[0:1]
        dp = [ [False]*n for i in range(n) ]
        # dp[i][j] 标记s[i:j]是否是一个回文串
        # 只有一个字符时一定是一个回文串
        for sz in range(1, n+1):
            # sz子串的长度
            for l in range(n-sz+1):
                # l 是区间的左端， r 是区间的右端
                r = l + sz - 1
                if s[l] == s[r]:
                    if l==r or l + 1 == r or dp[l+1][r-1]:
                        dp[l][r] = True
                        ans = s[l:r+1]
        return ans

print(Solution().longestPalindrome("babad"))
