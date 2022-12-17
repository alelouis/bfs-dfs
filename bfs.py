from collections import deque

def bfs(graph, start):
    """Breadth-First-Search"""
    queue, visited = deque([start]), []
    while queue:
        node = queue.popleft()
        visited.append(node)
        for neigh in graph[node]:
            if neigh not in visited:
                queue.append(neigh)
    return visited

def shortest_path(graph, start, end):
    """Shortest path (no weights)."""
    queue, visited, path = deque([start]), [], []
    while queue:
        node = queue.popleft()
        visited.append(node)
        path.append(node)
        for neigh in graph[node]:
            if neigh == end:
                return path + [neigh]
            elif neigh not in visited:
                queue.append(neigh)