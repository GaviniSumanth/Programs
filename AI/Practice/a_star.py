class Graph:
    def __init__(self, adjacency_list, heuristic) -> None:
        self.adjacency_list = adjacency_list
        self.heuristic = heuristic

    def getNeighbours(self, v):
        return self.adjacency_list[v]

    def h(self, n):
        return self.heuristic[n]

    def a_star(self, start_node, stop_node):
        open_list = set(start_node)
        closed_list = set()
        g = {}
        g[start_node] = 0
        parents = {}
        parents[start_node] = start_node
        while len(open_list) > 0:
            n = None
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v
            if n == None:
                print("No path exists")
                return
            if n == stop_node:
                reconst_path = []
                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start_node)
                reconst_path.reverse()
                print(f"Path found:{reconst_path}")
                return reconst_path
            for m, weight in self.getNeighbours(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_list:
                            closed_list.remove(n)
                            open_list.add(m)
            open_list.remove(n)
            closed_list.add(n)
        print("No path exists")
        return


h = {"A": 10, "B": 5, "C": 4, "D": 6, "E": 4}
adjacency_list = {
    "A": [("B", 1), ("C", 8), ("D", 12)],
    "B": [("D", 5)],
    "C": [("E", 12)],
    "D": [("E", 18)],
    "E": [],
}
print(Graph(adjacency_list, h).a_star("A", "E"))
