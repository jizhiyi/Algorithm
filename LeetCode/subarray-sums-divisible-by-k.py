class Solution:
    def subarraysDivByK(self, A, K) -> int:
        mp = {i:0 for i in range(K)}
        mp[0] = 1
        he, ans = 0, 0
        for i in A:
            he += i
            mod = he%K
            ans += mp.get(mod)
            mp[mod] += 1
        return ans


print(Solution().subarraysDivByK(A = [4,5,0,-2,-3,1], K = 5))
