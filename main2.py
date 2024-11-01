import graph_data
import permutation
import global_game_data
import main

for i in range (len(graph_data.graph_data)):
    permutation.find_hami_cycles()
    print(global_game_data.current_graph_index)
    main.change_graph()
    