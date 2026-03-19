class Graph:
    def __init__(self):
        self.graph = {}

    def add_edges(self,u ,v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])

        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

g = Graph()
g.add_edges(0,1)
g.add_edges(1,2)
g.add_edges(0,2)
print(g.graph)