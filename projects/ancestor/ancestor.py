
from util import Stack


class Graph:
    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Check if v1 and v2 vertexs exist.
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist.")


def earliest_ancestor(ancestors, starting_node):
    # ANCHOR: Create verts and edges for ancestors into graph

    # Instantiate graph
    graph = Graph()

    # Create verts
    for node in ancestors:
        # Parent
        graph.add_vertex(node[0])
        # Child
        graph.add_vertex(node[1])

    # Create edges
    for node in ancestors:
        graph.add_edge(node[1], node[0])

    # ANCHOR: Start DFS with starting node

    # Instantiate stack from util.
    stack = Stack()

    # Stack will hold a tuple (current node, path)
    stack.push([starting_node])

    # Visited holds node that has been visited as well as the path to get there
    visited = set()

    # While the stack is not empty...
    while stack.size() > 0:

        # Remove last element form stack and assign it to path.
        path = stack.pop()

        # Point vertex to last vert in path
        vertex = path[-1]

        if len(path) > len(visited):
            visited = path
        if len(path) == len(visited):
            if path[-1] < visited[-1]:
                visited = path

        for neighbor in graph.vertices[vertex]:
            path_copy = path.copy()
            path_copy.append(neighbor)
            stack.push(path_copy)

    if len(path) == 1:
        return -1

    return visited[-1]
