class BFS:
    def __init__(self) -> None:
        self.graph = {}

    def addEdge(self, x, y):
        if self.graph.get(x):
            self.graph[x].append(y)
        else:
            self.graph[x] = [y]

    def search(self, node):
        visited = [node]
        queue = [node]
        while queue:
            m = queue.pop(0)
            print(m, end=" ")
            for neighbour in self.graph.get(m) or []:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        print(end="\n")


b = BFS()
b.addEdge("5", "3")
b.addEdge("5", "7")
b.addEdge("3", "2")
b.addEdge("3", "4")
b.addEdge("7", "8")
b.addEdge("4", "8")
b.search("5")
