class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        l, r = min(bloomDay), max(bloomDay)
        n = len(bloomDay)


        def check(t):
            i = cnt = 0
            while i < n:
                if bloomDay[i] <= t:
                    tmp, j = 1, i+1
                    while j < n:
                        if bloomDay[j] > t:
                            i = j
                            break
                        tmp += 1
                        j += 1
                    else:
                        i = j
                    # print(tmp)
                    cnt += tmp//k
                i += 1
            # print('t, cnt', t, cnt)
            return cnt >= m

        while l < r:
            # print(l, r)
            mid = (l+r)//2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return r


print(Solution().minDays(bloomDay = [1,10,3,10,2], m = 3, k = 1))
print(Solution().minDays(bloomDay = [1,10,3,10,2], m = 3, k = 2))
print(Solution().minDays(bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3))
print(Solution().minDays(bloomDay = [1000000000,1000000000], m = 1, k = 1))
print(Solution().minDays(bloomDay = [1,10,2,9,3,8,4,7,5,6], m = 4, k = 2))