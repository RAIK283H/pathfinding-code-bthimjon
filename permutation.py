from itertools import permutations
import global_game_data
import graph_data

def is_valid_cycle(permutation, adj_list, graph_index):
    n = len(permutation)
    for i in range(n):
        # Current and next node in the cycle
        current_node = permutation[i]
        next_node = permutation[(i + 1) % n]
        
        # Check if there’s an edge from current_node to next_node in the specified graph
        if next_node not in adj_list[graph_index][current_node]:
            return False
    return True

def find_hamiltonian_cycles(adj_list, graph_index):
    # Get all vertices in the graph
    vertices = range(len(graph_data.graph_data[graph_index]))
    hamiltonian_cycles = []

    # Generate all permutations of vertices
    for perm in permutations(vertices):
        # Check if the permutation forms a valid Hamiltonian cycle in the specified graph
        if is_valid_cycle(perm, adj_list, graph_index):
            hamiltonian_cycles.append(perm)

    return hamiltonian_cycles


def makeAdjList(graph_index):
    adj_list =[]
    for i in range(len(graph_data.graph_data[graph_index])):
        adj_list.append([]) 
    for i in range (len(graph_data.graph_data[graph_index])):
        adj_list[graph_index].append(graph_data.graph_data[graph_index][i][1])
    print(adj_list)
    return adj_list
         

adj_list = makeAdjList(global_game_data.current_graph_index)
cycles = find_hamiltonian_cycles(adj_list, global_game_data.current_graph_index)
if cycles:
    for cycle in cycles:
        print("Hamiltonian Cycle:", cycle)
else:
    print("No Hamiltonian cycle found")


