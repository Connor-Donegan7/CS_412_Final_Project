
def tsp_approximate(graph):
    """
    Approximate solution to the Traveling Salesman Problem using a simple heuristic.

    Graph is represented as a dictionary where keys are nodes and values are lists of tuples (neighbor, weight).
    
    This approximate solution uses nearest neighbor heuristic to build a tour.

    """
    start_node = next(iter(graph))
    visited = set()
    tour = [start_node]
    visited.add(start_node)
    current_node = start_node
    while len(visited) < len(graph):
        unvisited_nodes = [node for node in graph if node not in visited]
        if not unvisited_nodes:
            break
        # Find the nearest unvisited node
        nearest_node = min(unvisited_nodes, key=lambda node: min(weight for neighbor, weight in graph[current_node] if neighbor == node))
        tour.append(nearest_node)
        visited.add(nearest_node)
        current_node = nearest_node
    # Return to start node to complete the tour
    tour.append(start_node)
    return tour

# Take input from command line argument or test file
# First get number of vertices and edges on one line Example: 3 3
# Now take input for amount of edges lines
# Example input for edge: A B 10.0
#
# Print our put as 1 line of length of tour weights
# Print nodes in order of tour in next line
if __name__ == "__main__":
    graph = {}
    n, m = map(int, input().strip().split())
    for _ in range(m):
        u, v, w = input().strip().split()
        w = float(w)
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, w))
        graph[v].append((u, w))  # Assuming undirected graph
    result = tsp_approximate(graph)
    total_weight = 0.0
    for i in range(len(result) - 1):
        u = result[i]
        v = result[i + 1]
        for neighbor, weight in graph[u]:
            if neighbor == v:
                total_weight += weight
                break
    print(total_weight)
    print(" ".join(result))