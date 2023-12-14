from queue import PriorityQueue
from collections import defaultdict


class BFS:
    def __init__(self, v) -> None:
        self.vertices = v
        self.graph = defaultdict(list)

    def search(self, src, target):
        visited = [False] * self.vertices
        pq = PriorityQueue()
        pq.put((0, src))
        visited[src] = True
        while not pq.empty():
            u = pq.get()[1]
            print(u, end=" ")
            if u == target:
                break
            for v, c in self.graph[u]:
                if not visited[v]:
                    visited[v] = True
                    pq.put((c, v))

    def addEdge(self, x, y, cost):
        self.graph[x].append((y, cost))
        self.graph[y].append((x, cost))


bfs = BFS(14)
bfs.addEdge(0, 1, 3)
bfs.addEdge(0, 2, 6)
bfs.addEdge(0, 3, 5)
bfs.addEdge(1, 4, 9)
bfs.addEdge(1, 5, 8)
bfs.addEdge(2, 6, 12)
bfs.addEdge(2, 7, 14)
bfs.addEdge(3, 8, 7)
bfs.addEdge(8, 9, 5)
bfs.addEdge(8, 10, 6)
bfs.addEdge(9, 11, 1)
bfs.addEdge(9, 12, 10)
bfs.addEdge(9, 13, 2)

source = 0
target = 11
bfs.search(source, target)
