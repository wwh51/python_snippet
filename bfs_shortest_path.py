
#It's a function to find shortest path in graph, BFS is used.
# dag is a dict, the key is the node tag. Every node can have up to 4 neighbors 
# dag['START'][0][0] is the node tag of the first neighbor 

visited = []
path = []
bfs_shortest_path(dag, 'START', visited, path)

def bfs_shortest_path(dag, current, visited, path):
  if current == 'END':
      path.append(current)
      return True

  if current in visited:
    return False;

  visited.append(current)
  path.append(current)
  for i in len(4):
    child_node = dag[top][i][0]    
    if bfs_shortest_path(dag, child_node, visited, path):
      return True
  del path[:-1]
  return False
