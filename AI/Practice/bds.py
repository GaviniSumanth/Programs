class Node:
    def __init__(self, vertex) -> None:
        self.vertex = vertex
        self.next = next


class BDS:
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.graph = [None] * self.vertices
        self.src_queue = []
        self.dest_queue = []
        self.src_visited = [False] * self.vertices
        self.dest_visited = [False] * self.vertices
        self.src_parent = [None] * self.vertices
        self.dest_parent = [None] * self.vertices

    def addEdge(self, src, dest):
        node = Node(dest)
        node.next = self.graph[src]
        self.graph[src] = node
        node = Node(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def bfs(self, direction="forward"):
        if direction == "forward":
            current = self.src_queue.pop(0)
            connected_node = self.graph[current]
            while connected_node:
                vertex = connected_node.vertex
                if not self.src_visited[vertex]:
                    self.src_queue.append(vertex)
                    self.src_visited[vertex] = True
                    self.src_parent[vertex] = current
                connected_node = connected_node.next
        else:
            current = self.dest_queue.pop(0)
            connected_node = self.graph[current]
            while connected_node:
                vertex = connected_node.vertex
                if not self.dest_visited[vertex]:
                    self.dest_queue.append(vertex)
                    self.dest_visited[vertex] = True
                    self.dest_parent[vertex] = current
                connected_node = connected_node.next

    def is_intersecting(self):
        for i in range(self.vertices):
            if self.src_visited[i] and self.dest_visited[i]:
                return i
        return -1

    def display_path(self, intersecting_node, src, dest):
        path = [intersecting_node]
        i = intersecting_node
        while i != src:
            path.append(self.src_parent[i])
            i = self.src_parent[i]
        path = path[::-1]
        i = intersecting_node
        while i != dest:
            path.append(self.dest_parent[i])
            i = self.dest_parent[i]
        print("PATH:")
        print(" ".join(list(map(str, path))))

    def search(self, src, dest):
        self.src_queue.append(src)
        self.src_parent[src] = -1
        self.src_visited[src] = True

        self.dest_queue.append(dest)
        self.dest_parent[dest] = -1
        self.dest_visited[dest] = True
        intersecting_node = -1
        while self.src_queue and self.dest_queue and intersecting_node == -1:
            self.bfs(direction="forward")
            self.bfs(direction="backward")
            intersecting_node = self.is_intersecting()
        if intersecting_node != -1:
            print(f"Path exists between {src} and {dest}")
            print(f"Intersection is at {intersecting_node}")
            self.display_path(intersecting_node, src, dest)
        else:
            print(f"Path does not exist between {src} and {dest}")


n = 15
src = 0
dest = 14
graph = BDS(n)
graph.addEdge(0, 4)
graph.addEdge(1, 4)
graph.addEdge(2, 5)
graph.addEdge(3, 5)
graph.addEdge(4, 6)
graph.addEdge(5, 6)
graph.addEdge(6, 7)
graph.addEdge(7, 8)
graph.addEdge(8, 9)
graph.addEdge(8, 10)
graph.addEdge(9, 11)
graph.addEdge(9, 12)
graph.addEdge(10, 13)
graph.addEdge(10, 14)

graph.search(src, dest)
