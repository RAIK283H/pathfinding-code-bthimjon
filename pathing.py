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
    return graph_data.test_path[global_game_data.current_graph_index]


def get_random_path():
    a = global_game_data.current_graph_index
    currentNode = 0
    end = len(graph_data.graph_data[a])-1

    #i got it to work for hitting the target just not hitting the end
    path = startToTarget(a,currentNode,global_game_data.target_node[a])
    currentNode = global_game_data.target_node[a]
    result = startToTarget(a,currentNode,end)
    for i in range(len(result)):
        path.append(result[i])
    return path
#b is 0 or the current index if you're keeping track of that
#create a function that takes beginning and target 
#while current index != target keep randomizing and go to the adjacency list of the current node

def startToTarget(currentGraph, currentNode, targetNode):
    path = [currentNode]
    while(currentNode != targetNode):
        adjacencyList = graph_data.graph_data[currentGraph][currentNode][1]
        currentNode =adjacencyList[random.randint(0,(len(adjacencyList)))]
        path.append(currentNode)
    return path

def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
