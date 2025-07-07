"""A graph that contains no cycle"""

from directed_graph import DirectedGraph

if __name__ == "__main__":
    graph = DirectedGraph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('A', 'C')
    
    graph.display()