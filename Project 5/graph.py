from stack_array import *  # Needed for Depth First Search
from queue_array import *  # Needed for Breadth First Search


class Vertex:
    '''Add additional helper methods if necessary.'''

    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.color = 'gray'

class Graph:
    '''Add additional helper methods if necessary.'''

    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        self.vertices_list = []  # list of all vertices in the graph

        specifications = open(filename, 'r')
        for line in specifications.readlines():  # construct the graph using the input file
            my_line = line.strip()
            my_edge = my_line.split()
            for v in my_edge:
                self.add_vertex(v)
            self.add_edge(my_edge[0], my_edge[1])

        specifications.close()

    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        for v in self.vertices_list:
            if v.id == key:  # if the vertex is in the list, return without adding it to the graph
                return
        self.vertices_list.append(Vertex(key))

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        for v in self.vertices_list:
            if v.id == key:
                return v
        return None

    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        vertex_1 = self.get_vertex(v1)
        vertex_2 = self.get_vertex(v2)

        vertex_1.adjacent_to.append(v2)
        vertex_2.adjacent_to.append(v1)

    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        verts = [v.id for v in self.vertices_list]
        verts.sort()
        return verts

    def conn_components(self):
        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        all_verts = self.get_vertices()

        verts_searched = []

        list_of_lists = []

        for id in all_verts:
            visited = []
            stack = Stack(100)
            if id not in verts_searched:
                V = self.get_vertex(id)
                verts_searched.append(id)
                visited.append(id)
                adjacent_list = V.adjacent_to
                for v in adjacent_list:
                    stack.push(v)
                while not stack.is_empty():
                    pop = stack.pop()
                    if pop not in visited:
                        visited.append(pop)
                        verts_searched.append(pop)
                    for vt in self.get_vertex(pop).adjacent_to:
                        if vt not in visited:
                            stack.push(vt)
                if visited:
                    visited.sort()
                    list_of_lists.append(visited)
        list_of_lists.sort()
        return list_of_lists

    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''

        vertex_q = Queue(100)

        list_connected_components = self.conn_components()
        for sections in list_connected_components:
            vertex_q.enqueue(self.get_vertex(sections[0]))
            while not vertex_q.is_empty():
                vertex = vertex_q.dequeue()
                if vertex.color == 'gray':
                    vertex.color = 'red'

                for vertices_label in vertex.adjacent_to:
                    vertices = self.get_vertex(vertices_label)
                    if vertex.color == 'red':
                        if vertices.color == 'gray':
                            vertices.color = 'black'
                            vertex_q.enqueue(vertices)
                        elif vertices.color == 'red':
                            return False
                    elif vertex.color == 'black':
                        if vertices.color == 'gray':
                            vertices.color = 'red'
                            vertex_q.enqueue(vertices)
                        elif vertices.color == 'black':
                            return False
        return True



