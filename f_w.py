import math
import global_game_data
import graph_data
import main


def distanceSolver(currentNode, targetNode):
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    return math.sqrt((graph[targetNode][0][0] - graph[currentNode][0][0])**2 + (graph[targetNode][0][1] - graph[currentNode][0][1])**2)

def adjacency_list_to_matrix():
    index = global_game_data.current_graph_index
    n= len(graph_data.graph_data[index])
    # Initialize distance matrix with infinity and 0 for self-loops

    dist = [[math.inf] * n for _ in range(n)]
    parent = [[None] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0  # Distance to self is zero
        parent[i][i] = i
        for j in range (len(graph_data.graph_data[index][1])):
            dist[i][j] = distanceSolver(i,j)
            parent[i][j] = i  # Set parent to the current node
    return dist, parent



def floyd_warshall(dist, parent):
    for k in range(len(dist)):
        for i in range(len(dist)):
            for j in range(len(dist)):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    parent[i][j] = parent[k][j]
    print(parent)

def FloydWarshallPath(P, i, j):
    path = []
    z = P[i][j]
    while z is not None: 
        path.insert(0,z)
        z = P[i,z]
    path.insert(0,i)
    path.append(j)
    return path


# Example Usage
index = global_game_data.current_graph_index
graph = graph_data.graph_data[index]
dist, parent = adjacency_list_to_matrix()
floyd_warshall(dist, parent)
print(parent)

for row in dist:
    print(row)
for row in parent:
    print(row)
        
path = FloydWarshallPath(parent, 0, len(graph)-1)
print("The shortest path: ")
print(path if path else "No path exists")
