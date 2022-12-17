from dfs import dfs_iterative, dfs_recursive
from bfs import bfs, shortest_path

graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B'],
         'F': ['C']}

print(f"DFS iterative: {dfs_iterative(graph, 'A')}")
print(f"DFS recursive: {dfs_recursive(graph, 'A', [])}")
print(f"BFS: {bfs(graph, 'A')}")
print(f"Shortest path: {shortest_path(graph, 'A', 'F')}")