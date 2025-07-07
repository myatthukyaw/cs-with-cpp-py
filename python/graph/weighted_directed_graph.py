class DirectedGraph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    def add_edge(self, vertex1, vertex2, weight=1):
        """Add a directed edge from vertex1 to vertex2 with a weight."""
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append((vertex2, weight))
        else:
            raise ValueError("Both vertices must be added before adding an edge.")
    
    def display(self):
        for vertex, edges in self.adjacency_list.items():
            formatted_edges = ', '.join(f"{neighbor}({weight})" for neighbor, weight in edges)
            print(f"{vertex}: {formatted_edges}")


if __name__ == "__main__":
    graph = DirectedGraph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    
    graph.add_edge('A', 'B', 5)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('A', 'C', 10)
    
    graph.display()
