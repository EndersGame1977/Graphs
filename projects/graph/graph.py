"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # NOTE
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Check if v1 and v2 vertexs exist.
        Add a directed edge to the graph.
        """
        # NOTE
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist.")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        pass  # TODO

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # NOTE
        #   Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)
        #   Create an empty Set to store visited vertices
        visited = set()
        #   While the queue is not empty...
        while q.size() > 0:
            #   Dequeue the first vertex
            v = q.dequeue()
            #   If that vertex has not been visted...
            if v not in visited:
                #   Mark it as visited
                print(v)
                visited.add(v)
                #   Then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # NOTE
        #   Create an empty stack and push the starting vertex ID
        s = Stack()
        s.push(starting_vertex)
        #   Create an empty Set to store visited vertices
        visited = set()
        #   While the stack is not empty...
        while s.size() > 0:
            #   Pop the first vertex
            v = s.pop()
            #   If that vertex has not been visted...
            if v not in visited:
                #   Mark it as visited
                print(v)
                visited.add(v)
                #   Then add all of its neighbors to the back of the stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # NOTE
        res = []

        def visit(vertex, visited=set()):
            nonlocal res
            if vertex not in visited:
                res.append(vertex)
                visited.add(vertex)
                for neighbor in self.vertices[vertex]:
                    visit(neighbor, visited)

        visit(starting_vertex)
        print(res)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # NOTE
        # visited holds Node that has been visited as well as the path to get there
        visited = set()
        # Queue will hold a tuple (currentVertex, path)
        q = Queue()
        q.enqueue([starting_vertex])

        while q.size() > 0:
            # Split queue into vertex and path
            path = q.dequeue()
            vertex = path[-1]
            # if vertex has not been visited or if it the starting_vertex
            if vertex not in visited:
                # add vertex to visited
                visited.add(vertex)
                # if it is the vertex we are looking for return the path
                if vertex == destination_vertex:
                    return path
                # add neighbors to stack
                for neighbor in self.vertices[vertex]:
                    q.enqueue(path + [neighbor])

        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # NOTE
        visited = set()
        s = Stack()
        s.push([starting_vertex])

        while s.size() > 0:
            path = s.pop()
            vertex = path[-1]

            if vertex not in visited:
                if vertex == destination_vertex:
                    return path

                visited.add(vertex)

                for neighbor in self.vertices[vertex]:
                    s.push(path + [neighbor])

    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
