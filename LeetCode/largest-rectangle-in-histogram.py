class Solution:
    def largestRectangleArea(self, heights) -> int:
        st = []
        ans = 0
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            while st and heights[i] < heights[st[-1]]:
                ans = max(ans, (i-st[-2]-1)*heights[st[-1]])
                del st[-1]
            st.append(i)
        return ans


print(Solution().largestRectangleArea([2,1,5,6,2,3]))
print(Solution().largestRectangleArea([1]))