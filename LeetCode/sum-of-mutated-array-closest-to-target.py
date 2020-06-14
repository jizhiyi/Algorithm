class Solution:
    def findBestValue(self, arr, target: int) -> int:
        n = len(arr)
        arr.sort()
        ans, mi = 0, target
        pos, he = 0, 0
        for i in range(arr[-1]+1):
            while i > arr[pos]:
                he += arr[pos]
                pos += 1
            temp = he + i*(n-pos)
            if mi > abs(target - temp):
                ans, mi = i, abs(target - temp)
        return ans


print(Solution().findBestValue(arr = [4,9,3], target = 10))
print(Solution().findBestValue(arr = [2,3,5], target = 10))
print(Solution().findBestValue(arr = [60864,25176,27249,21296,20204], target = 56803))