import graph_data
import permutation
import global_game_data
import main

#goes through all the graphs and finds the hamiltonian cycles
for i in range (len(graph_data.graph_data)):
    permutation.find_hami_cycles()
    #changes the graphs without using pyglet
    main.change_graph()
    