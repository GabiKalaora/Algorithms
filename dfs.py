def dfs(graph, node):
    visited = set()
    return def_helper(graph, node, visited)

def dfs_helper(graph, node, visited):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
            