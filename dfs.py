def dfs_iterative(graph, start):
    """Depth-First-Search, iterative version."""
    stack, visited = [start], []
    while stack:
        node = stack.pop()
        visited.append(node)
        for neigh in graph[node]:
            if neigh not in visited:
                stack.append(neigh)
    return visited

def dfs_recursive(graph, node, visited):
    """Depth-First-Search, recursive version."""
    visited.append(node)
    for neigh in reversed(graph[node]):  # In order to get same order as iterative
        if neigh not in visited:
            dfs_recursive(graph, neigh, visited) 
    return visited