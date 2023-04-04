import heapq
from .build_graph import load_graph, Graph, GraphNode


def dijkstra(start: str, end: str) -> list:
    graph = load_graph()
    # Initialize distances and visited sets
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    visited = set()

    # Use a priority queue to keep track of unexplored nodes
    queue = [(0, start)]

    while queue:
        # Get the node with the smallest distance so far
        current_distance, current_node = heapq.heappop(queue)

        # If we have already explored this node, skip it
        if current_node in visited:
            continue

        # Otherwise, add it to the visited set and check its neighbors
        visited.add(current_node)

        # If we have reached the end node, we can terminate early
        if current_node == end:
            break

        # Check the distance to each neighbor of the current node
        for neighbor, edge_weight in graph.nodes[current_node].edges.items():
            new_distance = current_distance + edge_weight

            # Update the distance to this neighbor if it's shorter than the current distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))

                # Store the previous node for this neighbor
                graph.nodes[neighbor].previous = current_node

    # If we have not found a path to the end node, return None
    if distances[end] == float('inf'):
        return None

    # Otherwise, construct the path from the end node to the start node
    path = []
    current_node = end
    while current_node != start:
        path.append(current_node)
        current_node = graph.nodes[current_node].previous
    path.append(start)
    return reversed(path)
