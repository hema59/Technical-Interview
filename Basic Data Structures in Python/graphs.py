from collections import deque
class graph:
    def __init__(self):
        self.graph = dict()

    def add_edge(self, edge : tuple):
        self.graph[edge[0] ] = edge[1]

    def add_graph(self, full_graph ):
        self.graph = full_graph

    def print_graph(self):
        print(self.graph)
    
    def dft(self, start, visited = None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end = " - ")
        for next in set(self.graph[start])-visited:
            self.dft(next, visited)
        return " |"

    def depth_traversal(self, start):
        if len(self.graph.keys() ) == 0 :
            return "Empty Graph"
        return self.dft(start)

    def bft(self, start):
        visited, queue = set(start), deque(start)
        while queue:
            vertex = queue.pop()
            print(vertex, end = " - ")
            for item in self.graph[vertex]:
                if item not in visited:
                    visited.add(item)
                    queue.append(item)
        return " |"

    def breadth_traversal(self, start):
        if len(self.graph.keys() ) == 0 :
            return "Empty Graph"
        return self.bft(start)

g = graph()
print("Create graph..")
temp = { 'A' : ['B','D'],
          'B' : ['C'],
          'C' : ['B','E'],
          'D' : ['A','F'],
          'E' : ['D'],
          'F' : ['G'],
          'G' : ['E','H'],
         }
g.add_graph(temp)
print("STATUS")
g.print_graph()
print("Adding edge.. ")
new_edge = ('H',[])
g.add_edge(new_edge)
print("STATUS")
g.print_graph()

print("\nDepth First Traversal from A")
g.depth_traversal('A')

print("\n\nBreadth First Traversal from A")
g.breadth_traversal('A')