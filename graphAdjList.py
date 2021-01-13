class Graph:
    def __init__(self, Vertexes, is_directed=False):
        self.vertexes = Vertexes
        self.adj_list = {}
        self.is_directed = is_directed

        for vertex in self.vertexes:
            self.adj_list[vertex] = []

    def print_adj_list(self):
        for vertex in self.vertexes:
            print(vertex, "->", self.adj_list[vertex])

    def add_edge(self, u, v):
        #depends if directed or undirected graph;
        #if undirected adjacency both ways
        self.adj_list[u].append(v)
        
        if not self.is_directed:
            self.adj_list[v].append(u)

    #degree is how many edges they have
    def degree(self, vertex):
        return len(self.adj_list[vertex])


if __name__ == '__main__':
    vertexes = ["A", "B",  "C", "D", "E"]
    graph = Graph(vertexes)
    # graph.add_edge("A", "B")

    all_edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("C", "E"), ("D", "E")]

    for u, v in all_edges:
        graph.add_edge(u, v)
        #for u in all_edges, returns first index A, A, B, C, C, D
        #for v in all_edges, returns second index B, C, D, D, E, E
        
    print("undirected graph:")
    graph.print_adj_list()

    print("Degree if vertex C is: " + str(graph.degree("C")) + '\n')

    graph2 = Graph(vertexes, is_directed=True)

    for u, v in all_edges:
        graph2.add_edge(u, v)
        #for u in all_edges, returns first index A, A, B, C, C, D
        #for v in all_edges, returns second index B, C, D, D, E, E
    
    print("directed graph:")
        
    graph2.print_adj_list()

    print("Degree if vertex C is: " + str(graph2.degree("C")))