class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if str(x) != str(x)[::-1]:
            return False
        return True


print(Solution().isPalindrome(121))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(10))
