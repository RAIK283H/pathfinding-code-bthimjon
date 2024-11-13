# Pathfinding Starter Code
My random path finder uses the current graph index, the current/starting node, and the target/ending node
In get_random_path it gathers all of this information and feeds it into a new method called startToTarget
    startToTarget randomly chooses nodes to visit until it hits the "target" node 
    then it returns the path of nodes visited to get to the target node
get_random_path then takes this information and saves it into an array 
then calls startToTarget to get from the target node that the last path ended on to the end of the graph
    startToTarget does the same thing using the new node information
get_random_path then saves this into an array and appends each node onto the path
then the path is returned 

In scoreboard I added the time it takes for the player to move to each individual node
This allows players to see how long in real time it takes for the player to travel between nodes


I used heapq to implement my priority queue for extra credit. 