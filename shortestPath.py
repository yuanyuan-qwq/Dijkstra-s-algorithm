#Using Python 
#Lum Fu Yuan B032110251 2BITI S1G2
import math #import package 'math'
#define Graph (vertices and edges) by using dictionary
graph = {
 'a': {'b': 359, 'c': 575, 'd': 578},
 'b': {'a': 359, 'c': 467, 'e': 480, 'f': 890},
 'c': {'a': 575, 'b': 467, 'd': 311, 'f': 935, 'g': 988},
 'd': {'a': 578, 'c': 311, 'h': 855, 'i': 663},
 'e': {'b': 480, 'f': 405},
 'f': {'e': 405, 'c': 935, 'g': 520, 'b': 890},
 'g': {'f': 520, 'c': 988, 'h': 615, 'l': 345},
 'h': {'d': 855, 'i': 793, 'g': 615, 'l': 406, 'k': 670},
 'i': {'d': 663, 'h': 793, 'j': 395},
 'j': {'i': 395, 'o': 567},
 'k': {'h': 670, 'l': 769, 'n': 367},
 'l': {'g': 345, 'h': 406, 'k': 769 , 'm': 752},
 'm': {'l': 752, 'n': 420, 'v': 275},
 'n': {'k': 367, 'o': 821, 'w': 564, 'v': 470, 'm': 420},
 'o': {'j': 567, 'p': 311, 't': 419, 'w': 741, 'n': 821},
 'p': {'o': 311, 'q': 486},
 'q': {'p': 486, 'r': 785, 's': 388, 'u': 355, 't': 391},
 'r': {'q': 785, 's': 408},
 's': {'q': 388, 'r': 408, 'u': 405},
 't': {'o': 419, 'q': 391, 'u': 419, 'y': 427, 'x': 489},
 'u': {'t': 419, 'q': 355, 's': 405, 'y': 339},
 'v': {'m': 275, 'n': 470, 'w': 233},
 'w': {'n': 564, 'o': 741, 'x': 177, 'v': 233},
 'x': {'w': 177, 't': 489, 'z': 537},
 'y': {'t': 427, 'u': 339, 'z': 497},
 'z': {'x': 537, 'y': 497}
}

# Define the start and goal destinations
start_point = 'a'
goal = 'z'

# Initialize the shortest distance dictionary
short_dist = {node: math.inf for node in graph}
short_dist[start_point] = 0

# Initialize the path_nodes dictionary
path_nodes = {}

# Process unvisited nodes
while graph:
    min_node = min(graph, key=short_dist.get)
    for neighbor, weight in graph[min_node].items():
        if short_dist[min_node] + weight < short_dist[neighbor]:
            short_dist[neighbor] = short_dist[min_node] + weight
            path_nodes[neighbor] = min_node
    graph.pop(min_node)

# Reconstruct the shortest path
node = goal
short_path = [node]
while node != start_point:
    node = path_nodes[node]
    short_path.insert(0, node)

# Print the results
if short_dist[goal] != math.inf:
    print(f'Shortest distance from {start_point} to {goal} is {short_dist[goal]}')
    print(f'The optimal path is: {short_path}')
else:
    print(f'No path found from {start_point} to {goal}')
