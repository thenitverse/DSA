class Graph:
    def adjacent_nodes(self, node):
        return self.graph[node]

    
    
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

network = Graph()
network.add_edge(0, 1)  # Alice(0) is friends with Bob(1)
network.add_edge(0, 2)  # Alice(0) is friends with Carol(2)
network.add_edge(1, 3)  # Bob(1) is friends with Dave(3)

# Who are Alice's friends?
print(network.adjacent_nodes(0))  # {1, 2}

# Who are Bob's friends?
print(network.adjacent_nodes(1))  # {0, 3}
