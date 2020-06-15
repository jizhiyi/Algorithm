
from  functools import reduce
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        ans = []
        for i in zip(*strs):
            if reduce(lambda a, b: a if a==b else None, i) is None:
                break
            ans.append(i[0])
        return ''.join(ans)


print(Solution().longestCommonPrefix(["flower","flow","flight"]))
print(Solution().longestCommonPrefix(["dog","racecar","car"]))

# print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))