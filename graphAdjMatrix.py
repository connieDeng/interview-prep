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

    # visited = set()
    def DFSRecursive(self, visited, v):
        # print(visited)
        if visited[v] == 0:
            print(v)
            visited[v] = 1
            for adjIndx in range(len(self.adj_matrix[v])):
                # print(visited)
                # print('\n')
                if self.adj_matrix[v][adjIndx] == 1 and visited[adjIndx] == 0:
                    self.DFSRecursive(visited, adjIndx)
        


if __name__ == '__main__':
    # vertexes = [ 0, 1, 2, 3, 4]
    # graph = Graph(vertexes, is_directed=True)
    # # graph.add_edge(0, 1)

    # all_edges = [(0,2), (0,1), (1,2), (2,0), (2,3), (3,3)]

    # for u, v in all_edges:
    #     graph.add_edge(u, v)
    #     #for u in all_edges, returns first index A, A, B, C, C, D
    #     #for v in all_edges, returns second index B, C, D, D, E, E
        
    # # print("undirected graph:")
    # # graph.print_adj_list()
    # print("DFS on first graph:")
    # graph.DFS(0)

    # # print("Degree if vertex C is: " + str(graph.degree("C")) + '\n')

    # try case 2
    vertexes = [0,1,2,3,4,5,6]
    graph2 = Graph(vertexes)
    # graph.add_edge(0, 1)

    all_edges2 = [(0,1), (0,2), (1,3), (1,4), (2,4), (3,5), (4,5), (5,6)]

    for u, v in all_edges2:
        graph2.add_edge(u, v)
        #for u in all_edges, returns first index A, A, B, C, C, D
        #for v in all_edges, returns second index B, C, D, D, E, E
        
    # print("undirected graph:")
    # graph.print_adj_list()
    print("DFS on second graph:")
    # graph2.DFS(2)
    visited = [0 for v in range(len(vertexes))]
    graph2.DFSRecursive(visited, 1)

    # print("Degree if vertex C is: " + str(graph.degree("C")) + '\n')