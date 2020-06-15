class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.dp = [[-1]*18 for i in range(n)]
        for i in range(1, n):
            self.dp[i][0] = parent[i]
        for i in range(1, 17):
            for j in range(1, n):
                tmp = self.dp[j][i-1] if self.dp[j][i-1] != -1 else 0
                self.dp[j][i] = self.dp[tmp][i-1]


    def getKthAncestor(self, node: int, k: int) -> int:
        p = 1
        for i in range(17):
            if k & p:
                node = self.dp[node][i]
            if node == -1:
                break
            p *= 2
        return node




# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)

# print(2 & 6)