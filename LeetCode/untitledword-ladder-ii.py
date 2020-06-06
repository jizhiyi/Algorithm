class Solution:
    def judeg_pass(self, a, b):
        """
        判断两个是否只改变一个字母能变成另一个
        :param a: 字符串一
        :param b: 字符串二
        :return: 返回能否，bool
        """
        if len(a) != len(b):
            return False
        flag = True
        for i, j in zip(a, b):
            if i != j:
                if not flag:
                    return False
                flag = False
        else:
            return True

    def dfs(self, pos, curn):
        """
        找寻答案
        :param pos: 当前位置
        :param curn: 当前位置离起点的距离
        :return: None
        """
        if pos == self.end and self.mi >= curn:
            if self.mi > curn:
                self.ans = []
                self.mi = curn
            # print(self.tmp)
            self.ans.append(self.tmp[:curn+1])
            return None

        if self.mi <= curn:
            return None
        for i in self.maps[pos]:
            if self.vis[i]:
                self.vis[i] = 0
                self.tmp[curn+1] = self.wordList[i]
                self.dfs(i, curn+1)
                self.vis[i] = 1


    def findLadders(self, beginWord: str, endWord: str, wordList):
        wordList.append(beginWord)
        # 找到终点字符串的位置
        self.wordList = wordList
        self.n = len(wordList)
        self.end, self.st = -1, self.n-1
        for i in range(self.n):
            if wordList[i] == endWord:
                self.end = i
                break
        # 没有终点字符串
        if self.end == -1:
            return []
        # 构建图
        self.maps = [[] for i in range(self.n)]
        for u in range(self.n):
            for v in range(u+1, self.n):
                if self.judeg_pass(wordList[u], wordList[v]):
                    self.maps[u].append(v)
                    self.maps[v].append(u)
        # print(self.maps)
        # dfs找寻答案
        self.ans = []
        self.tmp = ['']*self.n
        self.vis = [1] * self.n
        self.vis[self.st] = 0
        self.tmp[0] = beginWord
        self.mi = self.n+1
        self.dfs(self.st, 0)
        # print(self.mi)
        return self.ans




print(Solution().findLadders(beginWord = "hit",endWord = "cog",wordList = ["hot","dot","dog","lot","log","cog"]))
print(Solution().findLadders(beginWord = "hit",endWord = "cog",wordList = ["hot","dot","dog","lot","log"]))
