class Graph:
    def __init__(self,num_vertices):
        self.graph =[]
        for i in range(num_vertices):
            graph = []
            for j in range(num_vertices):
                graph.append(False)
            self.graph.append(graph)

    def add_edges(self,u,v):
        self.graph[u][v] = True
        self.graph[v][u] = True



num_vertices = int(input("Enter number of vertices: "))
g = Graph(num_vertices)

num_edges = int(input("Enter number of edges to add: "))
for _ in range(num_edges):
    u = int(input("Enter vertex u: "))
    v = int(input("Enter vertex v: "))
    g.add_edges(u, v)

print(g.graph)

