class Solution:
    def dailyTemperatures(self, T):
        n = len(T)
        ans = [0] * n
        st = []
        for i in range(n):
            while st and T[st[-1]] < T[i]:
                ans[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)
        return ans

print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))