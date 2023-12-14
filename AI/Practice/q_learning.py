import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

edges = [
    (0, 1),
    (1, 5),
    (5, 6),
    (5, 4),
    (1, 2),
    (1, 3),
    (9, 10),
    (2, 4),
    (0, 6),
    (6, 7),
    (8, 9),
    (7, 8),
    (1, 7),
    (3, 9),
]

goal = 10
G = nx.Graph()
G.add_edges_from(edges)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
plt.show()

MATRIX_SIZE = 11
M = np.matrix(np.ones(shape=(MATRIX_SIZE, MATRIX_SIZE)))
M *= -1
for point in edges:
    M[point] = 100 if point[1] == goal else 0
    M[point[::-1]] = 100 if point[0] == goal else 0
    M[goal, goal] = 100

Q = np.matrix(np.zeros(shape=(MATRIX_SIZE, MATRIX_SIZE)))
gamma = 0.75
initial_state = 1


def available_actions(state):
    return np.where(M[state] >= 0)[1]


def sample_next_action(available_actions):
    return int(np.random.choice(available_actions, 1)[0])


def update(current_state, action, gamma):
    max_index = np.where(Q[action] == np.max(Q[action]))[1]
    if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index, size=1)[0])
    else:
        max_index = int(max_index[0])
    max_value = Q[action, max_index]
    Q[current_state, action] = M[current_state, action] + gamma * max_value
    if np.max(Q) > 0:
        return np.sum(Q / np.max(Q) * 100)
    else:
        return 0


available_action = available_actions(initial_state)
action = sample_next_action(available_action)
update(initial_state, action, gamma)

scores = []
for i in range(1000):
    current_state = np.random.randint(0, int(Q.shape[0]))
    available_action = available_actions(current_state)
    if len(available_action) == 0:
        continue
    action = sample_next_action(available_action)
    score = update(current_state, action, gamma)
    scores.append(score)

current_state = initial_state
steps = [current_state]
while current_state != goal:
    next_step_index = np.where(Q[current_state] == np.max(Q[current_state]))[1]
    if next_step_index.shape[0] > 1:
        next_step_index = int(np.random.choice(next_step_index, size=1))
    else:
        next_step_index = int(next_step_index[0])
    steps.append(next_step_index)
    current_state = next_step_index

print("Most efficient path:")
print(steps)

plt.plot(scores)
plt.xlabel("No. of iterations")
plt.ylabel("Reward gained")
plt.show()
