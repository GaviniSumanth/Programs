class BFS:
    def __init__(self) -> None:
        self.graph = {}

    def addEdge(self, x, y):
        if self.graph.get(x):
            self.graph[x].append(y)
        else:
            self.graph[x] = [y]

    def displayGraph(self):
        for i in self.graph.items():
            print(f"{i[0]} --> {i[1]}")

    def __searchNoGoal(self, visited, queue):
        startNode = queue.pop()
        if startNode not in visited:
            visited.append(startNode)
            print(startNode, end=" ")
        for i in self.graph.get(startNode):
            if i not in visited:
                visited.append(i)
                queue.append(i)
                print(i, end=" ")
        if queue:
            return self.__searchNoGoal(visited, queue)
        print()

    def __search(self, visited, queue, x):
        startNode = queue.pop()
        if startNode not in visited:
            if startNode == x:
                print("Element Found")
                return True
            visited.append(startNode)
            print(startNode, end=" ")
        for i in self.graph.get(startNode):
            if i not in visited:
                if i == x:
                    print("Element Found")
                    return True
                visited.append(i)
                queue.append(i)
                print(i, end=" ")
        if queue:
            return self.__search(visited, queue)
        print("Element Not Found")
        return False

    def search(self, startNode, x=None, goal=False):
        visited = []
        queue = [startNode]
        if goal:
            self.__search(visited, queue, x)
        else:
            self.__searchNoGoal(visited, queue)


b = BFS()
b.addEdge(0, 1)
b.addEdge(0, 2)
b.addEdge(1, 2)
b.addEdge(2, 0)
b.addEdge(2, 3)
b.addEdge(3, 3)
b.displayGraph()
b.search(2)
