class Solution:
    def findLeastNumOfUniqueInts(self, arr, k: int) -> int:
        arr.sort()
        n = len(arr)
        cnt = []
        i = 0
        while i < n:
            tmp, j = 1, i+1
            while j<n:
                if arr[i] != arr[j]:
                    cnt.append(tmp)
                    i = j-1
                    break
                tmp += 1
                j += 1
            else:
                cnt.append(tmp)
                i = j-1
            i += 1
        cnt.sort()
        m = len(cnt)
        for i in range(m):
            k -= cnt[i]
            if k < 0:
                return m-i
        return 0





print(Solution().findLeastNumOfUniqueInts(arr = [5,5,4], k = 1))
print(Solution().findLeastNumOfUniqueInts(arr = [4,3,1,1,3,3,2], k = 3))