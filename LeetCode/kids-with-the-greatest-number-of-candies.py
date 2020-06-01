class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):
        mx = max(candies)
        return [ True if i+extraCandies >= mx else False for i in candies]


print(Solution().kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))