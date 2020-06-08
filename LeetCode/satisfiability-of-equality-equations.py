class Solution:
    def equationsPossible(self, equations) -> bool:
        father = [i for i in range(30)]
        noequations = []

        def findf(x):
            if x != father[x]:
                father[x] = findf(father[x])
            return father[x]
        for i in equations:
            if i[1] == '!':
                noequations.append(i)
            else:
                a, b = ord(i[0]) - 97, ord(i[3]) - 97
                father[findf(a)] = father[findf(b)]
        for i in noequations:
            a, b = ord(i[0]) - 97, ord(i[3]) - 97
            if findf(a) == findf(b):
                return False
        return True



print(Solution().equationsPossible(["a==b","b!=a"]))
print(Solution().equationsPossible(["b==a","a==b"]))
print(Solution().equationsPossible(["a==b","b==c","a==c"]))
print(Solution().equationsPossible(["a==b","b!=c","c==a"]))
print(Solution().equationsPossible(["c==c","b==d","x!=z"]))