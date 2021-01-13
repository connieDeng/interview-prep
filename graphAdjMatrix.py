class Graph:
    def __init__(self, Vertexes, is_directed=False):
        self.vertexes = Vertexes
        self.is_directed = is_directed

        self.adj_matrix = [ [ 0 for i in range(len(vertexes)) ] for j in range(len(vertexes)) ]
        # for i in range(len(self.adj_matrix)):
        #     for j in range(len(self.adj_matrix)):
        #         if i == j:
        #             self.adj_matrix[i][j] = 0
                    

    def print_adj_list(self):
        for rows in range(len(vertexes)):
            print(self.adj_matrix[rows])

    def add_edge(self, u, v):
        #depends if directed or undirected graph;
        #if undirected adjacency both ways
        self.adj_matrix[u][v] = 1
        if not self.is_directed:
            self.adj_matrix[v][u] = 1

    # #degree is how many edges they have
    # def degree(self, vertex):
    #     return len(self.adj_list[vertex])

    # s is passing the "root"/first node
    def DFS(self, s):
        visited = [0 for i in range(len(self.vertexes))]
        stack = []
        stack.append(s)

        while(len(stack)):
            elm = stack.pop()

            if visited[elm] != 1:
                visited[elm] = 1
                print(elm)
            
            for i in range(len(self.adj_matrix[elm])):
                if self.adj_matrix[elm][i] == 1 and visited[i] != 1:
                    stack.append(i)
                    # print(i)


if __name__ == '__main__':
    vertexes = [ 0, 1, 2, 3, 4]
    graph = Graph(vertexes, is_directed=True)
    # graph.add_edge(0, 1)

    all_edges = [(0,2), (0,1), (1,2), (2,0), (2,3), (3,3)]

    for u, v in all_edges:
        graph.add_edge(u, v)
        #for u in all_edges, returns first index A, A, B, C, C, D
        #for v in all_edges, returns second index B, C, D, D, E, E
        
    # print("undirected graph:")
    # graph.print_adj_list()
    print("DFS on first graph:")
    graph.DFS(0)

    # print("Degree if vertex C is: " + str(graph.degree("C")) + '\n')

    # try case 2
    vertexes = [ 0, 1, 2, 3]
    graph2 = Graph(vertexes)
    # graph.add_edge(0, 1)

    all_edges2 = [(2,0), (0,2), (0,1), (1,2), (2,3), (3,3)]

    for u, v in all_edges2:
        graph2.add_edge(u, v)
        #for u in all_edges, returns first index A, A, B, C, C, D
        #for v in all_edges, returns second index B, C, D, D, E, E
        
    # print("undirected graph:")
    # graph.print_adj_list()
    print("DFS on second graph:")
    graph2.DFS(2)

    # print("Degree if vertex C is: " + str(graph.degree("C")) + '\n')