# 方法一，栈
# class Solution:
#     def decodeString(self, s: str) -> str:
#         st = []
#         ans, cnt = '', 0
#         for i in s:
#             if i == '[':
#                 st.append((ans, cnt))
#                 ans, cnt = '', 0
#             elif i == ']':
#                 pans, pcnt = st.pop()
#                 ans = pans + ans*pcnt
#             elif '0' <= i and i <= '9':
#                 cnt = cnt*10 + int(i)
#             else:
#                 ans += i
#         return ans


# print(Solution().decodeString(s = "3[a]2[bc]"))
# print(Solution().decodeString(s = "3[a2[c]]"))
# print(Solution().decodeString(s = "2[abc]3[cd]ef"))

# 方法二，正则，字符串替换
import re
class Solution:
    def decodeString(self, s: str) -> str:
        pattern = re.compile(r'(\d+)\[(\w+)\]')
        res = pattern.findall(s)
        while res:
            for i in res:
                cnt, ts = i
                s = s.replace('%s[%s]'%(str(cnt), ts), ts*int(cnt))
            res = pattern.findall(s)
        return s


print(Solution().decodeString(s = "3[a]2[bc]"))
print(Solution().decodeString(s = "3[a2[c]]"))
print(Solution().decodeString(s = "2[abc]3[cd]ef"))