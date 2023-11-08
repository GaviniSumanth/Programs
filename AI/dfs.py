class DFS:
    def __init__(self) -> None:
        self.graph = {}

    def addEdge(self, x, y):
        if self.graph.get(x):
            self.graph[x].append(y)
        else:
            self.graph[x] = [y]
        if self.graph.get(y):
            self.graph[y].append(x)
        else:
            self.graph[y] = [x]

    def search(self, start, visited=[]):
        visited.append(start)
        print(start, end=" ")
        for i in self.graph[start]:
            if i not in visited:
                self.search(i, visited)


if __name__ == "__main__":
    g = DFS()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Depth First Traversal (starting from vertex 2)")

    # Function call
    g.search(2)
