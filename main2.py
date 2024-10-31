import graph_data
import permutation
import global_game_data
import main

for i in range (len(graph_data.graph_data)):
    permutation.find_hami_cycles()
    print(i)
    print(len(graph_data.graph_data))
    main.change_graph()