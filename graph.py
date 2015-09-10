class BFS:
    def __init__(self, graph):
        pass

class DFS:
    def __init__(self, graph):
        self.visited = [False] * graph.vertex_number
        self.graph = graph
    def check(vert):
        for vertex in self.graph.adjacent_vertex(vert):
            if not self.visited[vertex]:
                self.visited[vertex] = True
                self.dfs(vertex)


class Graph:
    def __init__(self):
        pass


class ListOfEdges(Graph):

    def __init__(self, edges, vertex_number):
        self.vertex_number = vertex_number
        self.edges = edges
        for edge in self.edges:
            edge.sort()
        self.edges.sort()

    def vertex_degree(self, vertex):
        degree = 0
        for edge in self.edges:
            if vertex in edge:
                degree += 1
        return degree

    def is_edge_between(self, first, second):
        return ([min(first, second), max(first, second)] in edges)

    def adjacent_vertex(self, vertex):
        adjacent_vertex = []
        potential_edges = self.edges
        for edge in potential_edges:
            if vertex in edge:
                edge.remove(vertex)
                adjacent_vertex.append(edge[0])
        return adjacent_vertex


class MatrixOfAdjacent(Graph):

    def __init__(self, matrix, vertex_number):
        self.vertex_number = vertex_number
        self.matrix = matrix

    def vertex_degree(self, vertex):
        return sum(self.matrix[vertex])

    def is_edge_between(self, first, second):
        return self.matrix[first][second]

    def adjacent_vertex(self, vertex):
        adjacent = []
        for vert in self.matrix[vertex]:
            if vert:
                adjacent.append(vert)
        return adjacent


class ListsOfAdjacents(Graph):

    def __init__(self, matrix, vertex_number):
        self.vertex_number = vertex.number
        self.matrix = matrix

    def vertex_degree(self, vertex):
        return len(self.matrix[vertex])

    def is_edge_between(self, first, second):
        return second in self.matrix[first]

    def adjacent_vertex(self, vertex):
        return self.matrix[vertex]
