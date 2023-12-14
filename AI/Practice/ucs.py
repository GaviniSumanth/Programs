from collections import defaultdict


class UCS:
    def __init__(self, graph, cost) -> None:
        self.graph = graph
        self.cost = cost

    def search(self, start, goal):
        answer = []
        queue = []
        for i in range(len(goal)):
            answer.append(10**8)
        queue.append([0, start])
        visited = {}
        count = 0
        while len(queue) > 0:
            queue = sorted(queue)
            p = queue.pop()
            p[0] *= -1
            if p[1] in goal:
                index = goal.index(p[1])
                if answer[index] == 10**8:
                    count += 1
                if answer[index] > p[0]:
                    answer[index] = p[0]
                queue.pop()
                if count == len(goal):
                    return answer
            if p[1] not in visited:
                for i in range(len(self.graph[p[1]])):
                    queue.append(
                        [
                            (p[0] + self.cost[p[1], self.graph[p[1]][i]]) * -1,
                            self.graph[p[1]][i],
                        ]
                    )


graph = defaultdict(list)
cost = {}
graph[0].append(1)
graph[0].append(3)
graph[3].append(1)
graph[3].append(6)
graph[3].append(4)
graph[1].append(6)
graph[4].append(2)
graph[4].append(5)
graph[2].append(1)
graph[5].append(2)
graph[5].append(6)
graph[6].append(4)

cost[(0, 1)] = 2
cost[(0, 3)] = 5
cost[(3, 1)] = 5
cost[(3, 6)] = 6
cost[(3, 4)] = 2
cost[(1, 6)] = 6
cost[(4, 2)] = 4
cost[(4, 5)] = 5
cost[(2, 1)] = 4
cost[(5, 2)] = 3
cost[(5, 6)] = 6
cost[(6, 4)] = 7
goal = []
goal.append(4)
ucs = UCS(graph, cost)
print("Minimum cost from 0 to 4 is", ucs.search(0, goal)[0])

graph = defaultdict(list)
cost = {}
graph[0].append(1)
graph[1].append(3)
graph[3].append(4)
graph[1].append(6)
graph[4].append(2)
graph[4].append(5)
graph[5].append(6)
graph[6].append(4)

cost[(0, 1)] = 12
cost[(1, 3)] = 35
cost[(1, 6)] = 26
cost[(3, 4)] = 32
cost[(4, 2)] = 24
cost[(4, 5)] = 25
cost[(5, 6)] = 36
cost[(6, 4)] = 27
goal = []
goal.append(4)
ucs = UCS(graph, cost)
print("Minimum cost from 0 to 4 is", ucs.search(0, goal)[0])
