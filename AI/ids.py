from collections import defaultdict


class Graph:
    def __init__(self, vertices) -> None:
        self.v = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DLS(self, src, target, maxDepth):
        if src == target:
            return True
        if maxDepth <= 0:
            return False
        for i in self.graph[src]:
            if self.DLS(i, target, maxDepth - 1):
                return True
        return False

    def IDS(self, src, target, maxDepth):
        for i in range(maxDepth):
            if self.DLS(src, target, i):
                return True
        return False


g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(4, 5)
g.addEdge(5, 6)
target = 6
maxdepth = 5
src = 0
print(g.IDS(src, target, maxdepth))
