import graph_data
import global_game_data
from numpy import random
import math
import heapq

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
    assert global_game_data.current_graph_index!=-1,"The current graph index is incorrect"
    #gets the current graph index and sets the beginning and ending nodes
    a = global_game_data.current_graph_index
    currentNode = 0
    end = len(graph_data.graph_data[a])-1

    #create a path using the random path calculated to the target node
    path = startToTarget(a,currentNode,global_game_data.target_node[a])
    assert len(path)>0,"Did not successfully add to the path"
    assert global_game_data.target_node[a] in path, "The path does not include the target node"

    #sets the current node equal to the target node(where the path ended)
    currentNode = global_game_data.target_node[a]

    #gets the remaining path from the target to the end node and append to the path
    result = startToTarget(a,currentNode,end)

    assert len(result)>0,"Did not successfully add to the path"
    assert result[len(result)-1]== end, "Did not successfully hit the target node"

    for i in range(1,len(result)):
        path.append(result[i])

    assert end in path, "The path does not include the exit node"

    for i in range (len(path)-1):
      assert path[i+1] in (graph_data.graph_data[a][path[i]][1]), "The path isn't valid"
    return path

#takes in the current graph index, the starting node, and the target end node
def startToTarget(currentGraph, currentNode, targetNode):
    assert targetNode>-1,"The target node is not configured properly"
    assert currentNode>-1,"The target node is not configured properly"

    #starts an array for the path with the beginning node
    path = [currentNode]

    #continues to choose a random node until it is the target node
    while(currentNode != targetNode):
        adjacencyList = graph_data.graph_data[currentGraph][currentNode][1]
        currentNode =adjacencyList[random.randint(0,(len(adjacencyList)))]
        path.append(currentNode)

    assert len(path)>0,"No new nodes were added to the path" 
    assert path[len(path)-1]==targetNode, "Did not end on the target node"
    return path

def get_dfs_path():
  #sets the index and end node
  a = global_game_data.current_graph_index
  end = len(graph_data.graph_data[a])-1

#gets the path to the target node and checks that the path includes the target node
  path = dfsToTarget(a, 0, global_game_data.target_node[a])
  assert global_game_data.target_node[a] in path, "The path does not include the target node"

#gets the path to the end node and checks that it is in the path
  result = dfsToTarget(a, global_game_data.target_node[a], end)
  for i in range(1,len(result)):
        path.append(result[i])
  assert end in path, "The path does not include the exit node"

#checks that all nodes in the path are connected in the adjacency list
  for i in range (len(path)-1):
      assert path[i+1] in (graph_data.graph_data[a][path[i]][1]), "The path isn't valid"
  return path

def dfsToTarget(graph, currentNode, targetNode, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    
    visited.add(currentNode)
    path.append(currentNode)
    
    #checks if the current node is the target node
    if currentNode == targetNode:
        return path  # return the path to the target node
    
    #visits all the neighbors
    for neighbor in graph_data.graph_data[graph][currentNode][1]:
        if neighbor not in visited:
            result = dfsToTarget(graph, neighbor, targetNode, visited, path)
            if result:  #if target is found return all the nodes to the path
                return result
    
    #if target not found in this path backtrack
    path.pop()
    return None

def get_bfs_path():
    #sets the graph index and end node
    a = global_game_data.current_graph_index
    end = len(graph_data.graph_data[a])-1

    #gets the path to the target node and checks if the target is in the path
    path = bfsToTarget(a, 0, global_game_data.target_node[a])
    assert global_game_data.target_node[a] in path, "The path does not include the target node"

#gets the path to the end node and checks
    result = bfsToTarget(a, global_game_data.target_node[a], end)
    for i in range(1,len(result)):
        path.append(result[i])
    assert end in path, "The path does not include the exit node"

#checks that all the nodes in the path are connected
    for i in range (len(path)-1):
      assert path[i+1] in (graph_data.graph_data[a][path[i]][1]), "The path isn't valid"
    return path

def bfsToTarget(graph, currentNode, targetNode):
    queue = [(currentNode, [currentNode])]
    visited = set()
    
    while queue:
        currentNode, path = queue.pop(0)
        
        #if target node is found, return the path
        if currentNode == targetNode:
            return path
        
        #if node is not visited, explore its neighbors
        if currentNode not in visited:
            visited.add(currentNode)
            
            #go to all the neighbors of the current node
            for neighbor in graph_data.graph_data[graph][currentNode][1]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    
    #if target node is not found
    return None

def get_dijkstra_path():
    a = global_game_data.current_graph_index
    end = len(graph_data.graph_data[a])-1

    #gets the path to the target node and checks if the target is in the path
    path = dijkstrasToTarget(a, 0 ,global_game_data.target_node[a])
    assert global_game_data.target_node[a] in path, "The path does not include the target node"

    #gets the path to the end node and checks
    result = dijkstrasToTarget(a, global_game_data.target_node[a], end)
    for i in range(1,len(result)):
        path.append(result[i])

    #assertions
    assert end in path, "The path does not include the exit node"
    assert path[0] == 0, "The path does not begin with the start node"
    assert path[len(path)-1]== end, "The path does not end with the exit node"
    for i in range (len(path)-1):
        assert path[i+1] in graph_data.graph_data[global_game_data.current_graph_index][path[i]][1], "The next node is not in the adjacency list for the previous node"
    return path


    

def dijkstrasToTarget(graphIndex,startNode,targetNode):
    #sets the distances for all the nodes, the distance to the start node is 0
    distances = [0]
    for node in graph_data.graph_data[graphIndex]:
        distances.append(float('infinity'))
    previous = {startNode: None}
    queue = [(0, startNode)]
    visited = set()
    
    #while the queue isn't empty
    while queue:
        current_distance, currentNode = heapq.heappop(queue)

        #checks if the target node is the current node
        if currentNode == targetNode:
            path = []
            #appends and returns the path to the target node
            while currentNode is not None:
                path.append(currentNode)
                currentNode = previous[currentNode]
            return path[::-1]
        
        if current_distance > distances[currentNode]:
            continue

        visited.add(currentNode)

        adjacencyList = graph_data.graph_data[graphIndex][currentNode][1]
        #checks every neighbor in the adjacency list
        for neighbor in adjacencyList:
            if neighbor not in visited:
                #adds the distance to the neighbor node to the current node
                new_distance = current_distance + distanceSolver(currentNode, neighbor)

                #if the new distance is shorter than the current distance
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous[neighbor] = currentNode 
                    heapq.heappush(queue, (new_distance, neighbor))
    
    #return none if the target node isn't found
    return None


#solves for the distance between the current and target node
def distanceSolver(currentNode, targetNode):
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    return math.sqrt((graph[targetNode][0][0] - graph[currentNode][0][0])**2 + (graph[targetNode][0][1] - graph[currentNode][0][1])**2)