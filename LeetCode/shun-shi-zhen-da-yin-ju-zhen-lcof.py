class Solution:
    def go(self, x, y, d):
        # print(x, y, d)
        self.ans.append(self.matrix[x][y])
        self.matrix[x][y] = None
        if len(self.ans) == self.n*self.m:
            return None
        for i in range(4):
            td = (d+i)%4
            tx, ty = self.d[td][0]+x, self.d[td][1]+y
            # print('tx, ty', tx, ty)
            if tx < 0 or ty < 0 or tx>=self.n or ty>=self.m or self.matrix[tx][ty] is None:
                continue
            self.go(tx, ty, td)
            return None

    def spiralOrder(self, matrix):
        if not matrix:
            return []
        self.matrix = matrix
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.ans = []
        self.d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.go(0, 0, 0)
        return self.ans


print(Solution().spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(Solution().spiralOrder(matrix = []))