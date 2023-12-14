import random


def randomSolution(tsp):
    states = [i for i in range(len(tsp))]
    solution = []
    for i in range(len(tsp)):
        state = states[random.randint(0, len(states) - 1)]
        solution.append(state)
    return solution


def routeLength(tsp, solution):
    routeLength = 0
    for i in range(len(solution)):
        routeLength += tsp[solution[i - 1]][solution[i]]
    return routeLength


def getNeighbours(solution):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i], neighbour[j] = solution[j], solution[i]
            neighbours.append(neighbour)
    return neighbours


def getBestNeighbour(tsp, neighbours):
    best_rlen = routeLength(tsp, neighbours[0])
    best_neighbour = neighbours[0]
    for neighbour in neighbours:
        current_rlen = routeLength(tsp, neighbour)
        if current_rlen < best_rlen:
            best_rlen = current_rlen
            best_neighbour = neighbour
    return best_neighbour, best_rlen


def hillClimbing(tsp):
    current_solution = randomSolution(tsp)
    current_rlen = routeLength(tsp, current_solution)
    neighbours = getNeighbours(current_solution)
    best_neighbour, best_neighbour_rlen = getBestNeighbour(tsp, neighbours)
    while best_neighbour_rlen < current_rlen:
        current_solution = best_neighbour
        current_rlen = best_neighbour_rlen
        neighbours = getNeighbours(current_solution)
        best_neighbour, best_neighbour_rlen = getBestNeighbour(tsp, neighbours)
    return current_solution, current_rlen


def randomTSP(states):
    tsp = [[0] * states for i in range(states)]
    for i in range(states):
        for j in range(i + 1):
            tsp[i][j] = tsp[j][i] = random.randint(1, 1000)
    return tsp


tsp = randomTSP(10)
print("TSP:")
for i in tsp:
    print(i)
print("\n", end="")
output = hillClimbing(tsp)
print(f"Solution : {output[0]}")
print(f"Length   : {output[1]}")
