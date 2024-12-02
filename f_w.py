import math
import global_game_data
import graph_data
import main


def distanceSolver(currentNode, targetNode):
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    return math.sqrt((graph[targetNode][0][0] - graph[currentNode][0][0])**2 + (graph[targetNode][0][1] - graph[currentNode][0][1])**2)

def adjacency_list_to_matrix():
    index = global_game_data.current_graph_index
    n = len(graph_data.graph_data[index])  # Number of nodes

    # Initialize distance and parent matrices
    dist = [[math.inf] * n for _ in range(n)]
    parent = [[None] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0
        parent[i][i] = i

        for j in graph_data.graph_data[index][i][1]:
            dist[i][j] = distanceSolver(i, j)
            parent[i][j] = i 

    return dist, parent


def floyd_warshall(dist, parent):
    for k in range(len(dist)):
        for i in range(len(dist)):
            for j in range(len(dist)):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    parent[i][j] = parent[k][j]


def FloydWarshallPath(P, i, j):
    if P[i][j] is None:
        return None

    path = [j]
    while j != i:
        j = P[i][j]
        if j is None:
            return None
        path.insert(0, j)
    return path

index = global_game_data.current_graph_index
graph = graph_data.graph_data[index]
dist, parent = adjacency_list_to_matrix()
floyd_warshall(dist, parent)

for row in dist:
    print(row)
        
path = FloydWarshallPath(parent, 0, len(graph)-1)
print("The shortest path: ")
print(path if path else "No path exists")
