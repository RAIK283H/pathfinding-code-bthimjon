import graph_data
import global_game_data
from numpy import random

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    print(graph_data.test_path[global_game_data.current_graph_index])
    return graph_data.test_path[global_game_data.current_graph_index]


def get_random_path():
    #graph_data[a] = gives you graph at index a
    #graph_data[a][0] = start node of graph a
    #graph_data[a][length-1] = exit node of graph a
    #graph_data[a][b][0] = x-y coordinates as tuple of point b in graph a
    #graph_data[a][b][1] = adjacency list of point b in graph a
    #randomly generate a based on the length of graph_data then randomly generate b based on the length of graph_data[a]
    #then randomly generated a new point and check if its in the adjacency list 
    a = global_game_data.current_graph_index
    b = random.randint((len(graph_data.graph_data[a])-1))
    print(global_game_data.current_graph_index)

    print(graph_data.graph_data[a][b][1])
    return graph_data.graph_data[a][b][1]


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
