
from util import Queue


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
        # Build edges in reverse
        graph.add_edge(node[1], node[0])

    # ANCHOR: Start BFS with starting node

    # Instantiate queue from util.
    queue = Queue()

    # queue will hold a tuple (current node, path)
    queue.enqueue([starting_node])
    max_path_len = 1
    earliest_ancestor = -1

    # While the queue is not empty...
    while queue.size() > 0:

        # Remove last element form queue and assign it to path.
        path = queue.dequeue()

        # Point vertex to last vert in path
        vertex = path[-1]

        if (len(path) >= max_path_len and vertex < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = vertex
            max_path_len = len(path)
        for neighbor in graph.vertices[vertex]:
            path_copy = list(path)
            path_copy.append(neighbor)
            queue.enqueue(path_copy)
    return earliest_ancestor
