from queue import Queue


class Solution:
    def topsort(self, n, maps, ru):
        res = []
        que = Queue()
        for i in range(n):
            if ru[i] == 0:
                que.put(i)
        while not que.empty():
            res.append(que.get())
            for i in maps[res[-1]]:
                ru[i] -= 1
                if ru[i] == 0:
                    que.put(i)
        return res if len(res) == n else []

    def findOrder(self, numCourses: int, prerequisites):
        maps = [[] for i in range(numCourses)]
        ru = [0 for i in range(numCourses)]
        for e in prerequisites:
            maps[e[1]].append(e[0])
            ru[e[0]] += 1
        return self.topsort(numCourses, maps, ru)


print(Solution().findOrder(2, [[1, 0]]))
print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
