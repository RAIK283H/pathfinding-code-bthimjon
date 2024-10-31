import graph_data
import permutation

# Find Hamiltonian cycles
cycles = find_hamiltonian_cycles(graph_data[global_game_data.current_graph_index])
if cycles:
    for cycle in cycles:
        print("Hamiltonian Cycle:", cycle)
else:
    print("No Hamiltonian cycle found")