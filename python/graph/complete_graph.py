"""
A graph in which there is a direct edge between every pair of vertices
in undirected graph, n vertices will have n(n-1)/2 edges
in directed graph, n vertices will have n(n-1) edges
"""
from directed_graph import DirectedGraph
from undirected_graph import UndirectedGraph

if __name__ == "__main__":
    graph = DirectedGraph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'C')
    graph.add_edge('B', 'A')
    graph.add_edge('C', 'A')
    graph.add_edge('C', 'B')
    
    graph.display()