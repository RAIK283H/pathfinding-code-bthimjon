from itertools import permutations

def is_valid_cycle(permutation, adj_list):
    n = len(permutation)
    for i in range(n):
        # Check if each pair of consecutive vertices in the cycle has an edge
        if permutation[i] not in adj_list[permutation[(i + 1) % n]]:
            return False
    return True

def find_hamiltonian_cycles(adj_list):
    # Get all vertices in the graph
    vertices = list(adj_list.keys())
    n = len(vertices)
    hamiltonian_cycles = []

    # Generate all permutations of vertices using SJT
    for perm in permutations(vertices):
        # Check if the permutation fokrms a valid Hamiltonian cycle
        if is_valid_cycle(perm, adj_list):
            hamiltonian_cycles.append(perm)

    return hamiltonian_cycles

# Example usage
adj_list = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

