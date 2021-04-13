class Graph:
    def __init__(self):
        self.graph = {}

    def print_graph(self):
        for i in self.graph:
            print(i, ' : ', '->'.join(str(j) for j in self.graph[i]))

    def add_edge(self, from_node, to_node):
        if from_node in self.graph:
            self.graph[from_node].append(to_node)

    def bfs(self, starting_node):
        visited = set()
        queue = []
        visited.add(starting_node)
        queue.append(starting_node)

        while queue:
            node = queue.pop(0)
            for adj_node in self.graph[node]:
                if adj_node not in visited:
                    queue.append(adj_node)
                    visited.add(adj_node)
        return visited
