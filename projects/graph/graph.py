"""Simple graph implementation"""
from util import Stack, Queue  # These may come in handy
visited_recur = []

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """Add a vertex to the graph."""
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """Add a directed edge to the graph."""
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("nonexistant vertices")

    def get_neighbors(self, vertex_id):
        """Get all neighbors (edges) of a vertex."""
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """Print each vertex in breadth-first order beginning from starting_vertex."""
        # initialize an empty queue and set to retain visited verts
        # enqueue the starting vert to the empty queue
        q = Queue()
        visited = set()
        q.enqueue(starting_vertex)

        # While queue isn't empty:
        while q.size() > 0:
            
            # dequeue the first in vert in the queue and set it to the value of current
            cur = q.dequeue()

            # if current vert is not in the visited set
            if cur not in visited:
                print(cur) # "Visit" the node

                # and add the current vert to the visited set
                visited.add(cur)

                # for each neighbor of the current vert found using the get_neighbors method
                for neighbor in self.get_neighbors(cur):
                    # enqueue the neighbor to the queue
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """Print each vertex in depth-first order beginning from starting_vertex."""
        # initialize an empty stack and set to retain visited verts
        # push the starting vert to the empty stack
        q = Stack()
        visited = set()
        q.push(starting_vertex)

        # While queue isn't empty
        while q.size() > 0:

            # pop the last in vert in the stack and set it to the value of current
            cur = q.pop()

            # if current vert is not in the visited set
            if cur not in visited:
                print(cur) # "Visit" the node

                # and add the current vert to the visited set
                visited.add(cur)

                # for each neighbor of the current vert found using the get_neighbors method
                for neighbor in self.get_neighbors(cur):
                    # push the neighbor to the stack
                    q.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """Print each vertex in depth-first order beginning from starting_vertex. This should be done using recursion."""
        # print the starting vertex, which will be recursed over and always be the first vertex in
        # initialized a empty array outside of the Class
        print(starting_vertex)

        # if the starting vertex is not in the visited verts array
        if starting_vertex not in visited_recur:
            
            # append to the array the starting vertex
            visited_recur.append(starting_vertex)
            
            # set the neighbors using the get_neighbors method to those of the starting vertext
            neighbors = self.get_neighbors(starting_vertex)
            
            # iterate over the neighbors
            for i in neighbors:
            
                # if the neighbor is not in the visited verts array, recurse over it (print, then neighbors, then recurse)
                if i not in visited_recur:            
                    self.dft_recursive(i)

    def bfs(self, starting_vertex, destination_vertex):
        """Return a list containing the shortest path from starting_vertex to destination_vertex in breath-first order."""
        # create an empty queue
        # enqueue a PATH to the starting vertex
        path = [starting_vertex]
        q = Queue()
        q.enqueue(path)

        # while the queue is not empty
        while q.size() > 0:
            
            # dequeue the first path, set to current
            cur = q.dequeue()

            # grab the last vertex from the path
            # if it's the target, aka destination vertex, return current as it's the path
            if cur[-1] == destination_vertex:
                return cur
            
            # if the last vertex in the path is not the target, aka destination vertex,
            # add a path to its neighbors to the back of the queue
            for i in self.get_neighbors(cur[-1]):
                # copy the path and set to explore next
                # enqueue the path to explore next to the queue
                explore_next = [*cur, i]
                q.enqueue(explore_next)

    def dfs(self, starting_vertex, destination_vertex):
        """Return a list containing a path from starting_vertex to destination_vertex in depth-first order."""
        # create an empty queue
        # enqueue a PATH to the starting vertex
        path = [starting_vertex]
        q = Stack()
        q.push(path)

        # while the queue is not empty
        while q.size() > 0:

            # pop the first path, set to current
            cur = q.pop()

            # grab the last vertex from the path
            # if it's the target, aka destination vertex, return current as it's the path
            if cur[-1] == destination_vertex:
                return cur

            # if the last vertex in the path is not the target, aka destination vertex,
            # add a path to its neighbors to the back of the stack
            for i in self.get_neighbors(cur[-1]):
                # copy the path and set to explore next
                # push the path to explore next to the stack                
                explore_next = [*cur, i]
                q.push(explore_next)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=list(), visited=list()):
        """Return a list containing a path from starting_vertex to destination_vertex in depth-first order. This should be done using recursion."""

        # initalize a path equal to the path plus the starting vert
        path += [starting_vertex]

        # if the starting vert is the destination vertex, i.e. the target, return the path
        if starting_vertex == destination_vertex:
            return path
        
        # if the starting vert is not in the visited list, append the starting vert to the visited list
        if starting_vertex not in visited:
            visited.append(starting_vertex)

            # for each neighbor that's a neighbor of the starting vert, per the get_neighbors method
            for i in self.get_neighbors(starting_vertex):
                # if the neighbor is not in the visited listed
                if i not in visited:
                    # set explore next to recur the neighbor as starting vert, destination vert remains, path as a list of the cur path, and leave visited alone
                    explore_next = self.dfs_recursive(i, destination_vertex, list(path), visited)
                    # if explore next has a value, return it which starts the recursive process
                    if explore_next:
                        return explore_next
            
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
    print(graph.dfs_recursive(1, 6))
