class Graph:
    def depth_first_search(self, start_vertex):
        visited = []
        self.depth_first_search_r(visited, start_vertex)
        return visited

    def depth_first_search_r(self, visited, current_vertex):
        visited.append(current_vertex)
        sorted_list = sorted(self.graph[current_vertex])
        for current in sorted_list:
            if current not in visited:
                self.depth_first_search_r(visited, current)

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    


g = Graph()
g.add_edge("New York", "London")
g.add_edge("New York", "Cairo")
g.add_edge("New York", "Tokyo")
g.add_edge("London", "Dubai")

result = g.depth_first_search("New York")
print(result)