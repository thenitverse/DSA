class Graph:
    def unconnected_vertices(self):
         results = []
         for k,v in self.graph.items():
            if not v:
                results.append(k)
         return results 
        
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}

    def add_node(self, u):
        if u not in self.graph:
            self.graph[u] = set()


g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_node(3)
g.add_node(4)

print(g.graph)

print(g.unconnected_vertices())
# [3, 4]