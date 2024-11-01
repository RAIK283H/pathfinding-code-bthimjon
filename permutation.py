from itertools import permutations
import global_game_data
import graph_data

def sjt_permutation(graphIndex):
    elements = range(1, len(graph_data.graph_data[graphIndex]) - 1)
    return list(permutations(elements))

def is_valid_hami_cycle(permutation, end, graphIndex):
    cycle = [0] + list(permutation) + [end]
    
    for i in range(len(cycle) - 1):
        node = cycle[i]
        next_node = cycle[i + 1]

        adj_nodes = graph_data.graph_data[graphIndex][node][1]
        
        if next_node not in adj_nodes:
            return False
    return True 

def find_hami_cycles():
    index = global_game_data.current_graph_index
    end = len(graph_data.graph_data[index]) - 1
    valid_cycles = []

    for perm in sjt_permutation(index):
        if is_valid_hami_cycle(perm, end, index):
            valid_cycles.append([0] + list(perm) + [end])

    if valid_cycles:
        for cycle in valid_cycles:
            print("Valid Hamiltonian Cycle(s):", cycle)
        return valid_cycles
    else:
        print("No valid Hamiltonian cycle exists")
        return -1

