class UndirectedGraph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1) 
    
    def display(self):
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex}: {', '.join(map(str, edges))}")


# Example usage
if __name__ == "__main__":
    graph = UndirectedGraph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('A', 'C')
    
    graph.display()