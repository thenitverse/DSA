class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def breadth_first_search(self, v):
        visited_list = []
        que = []
        que.append(v)
        while que:
            m = que.pop(0)
            visited_list.append(m)
            sorted_list = sorted(self.graph[m])
            for i in sorted_list:
                if i not in visited_list and i not in que:
                    que.append(i)
        return visited_list


# --- Tests ---
graph = Graph()
edges = [
    ("New York", "London"),
    ("New York", "Cairo"),
    ("New York", "Tokyo"),
    ("London", "Dubai"),
]

for edge in edges:
    graph.add_edge(edge[0], edge[1])

result = graph.breadth_first_search("New York")
expected = ["New York", "Cairo", "London", "Tokyo", "Dubai"]

print("Result:  ", result)
print("Expected:", expected)
print("Pass" if result == expected else "Fail")