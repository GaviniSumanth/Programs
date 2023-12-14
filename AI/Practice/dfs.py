class DFS:
    def __init__(self) -> None:
        self.graph = {}

    def addEdge(self, x, y):
        if self.graph.get(x):
            self.graph[x].append(y)
        else:
            self.graph[x] = [y]

    def search(self, node, visited=[]):
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            for neighbour in self.graph.get(node) or []:
                self.search(neighbour, visited)


d = DFS()
d.addEdge("5", "3")
d.addEdge("5", "7")
d.addEdge("3", "2")
d.addEdge("3", "4")
d.addEdge("7", "8")
d.addEdge("4", "8")
d.search("5")
