from constants import EACH_LINES_DISTANCE_TO_PREVIOUS_STATION_LIST

class GraphNode:
    def __init__(self, name):
        self.name = name
        self.edges = {}

    def add_edge(self, node, weight):
        self.edges[node] = weight
    
class Graph:
    def __init__(self):
        self.nodes = {}
        self.node_names = set()

    def add_node(self, name):
        if(name not in self.node_names):
            node = GraphNode(name)
            self.nodes[name] = node
            self.node_names.add(name)

    def add_edge(self, node1, node2, weight):
        self.nodes[node1].add_edge(node2, weight)
        self.nodes[node2].add_edge(node1, weight)


def create_graph():
    graph = Graph()

    for line in EACH_LINES_DISTANCE_TO_PREVIOUS_STATION_LIST:
        edges = EACH_LINES_DISTANCE_TO_PREVIOUS_STATION_LIST[line]
        first_stop = True
        prev_node = ""
        for edge in edges:
            graph.add_node(edge[0])
            if not first_stop:
                graph.add_edge(prev_node, edge[0], edge[1])
            else:
                first_stop = False
            prev_node = edge[0]
            
    for node_name, node in graph.nodes.items():
        print(f"{node_name}: {node.edges}")
    
    return graph