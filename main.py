import heapq

def dijkstra_shortest_path(graph, start, goal):
    """
    Compute shortest path with positive weights.
    Graph is treated as UNDIRECTED (both directions), as tests expect.
    """

    # If start or goal missing
    if start not in graph or goal not in graph:
        return ([], None)

    # Build UNDIRECTED adjacency list
    undirected = {}
    for node in graph:
        undirected.setdefault(node, [])
        for neighbor, w in graph[node]:
            undirected[node].append((neighbor, w))
            undirected.setdefault(neighbor, [])
            undirected[neighbor].append((node, w))

    # Dijkstra setup
    dist = {node: float('inf') for node in undirected}
    dist[start] = 0
    parent = {start: None}
    heap = [(0, start)]

    while heap:
        curr_cost, node = heapq.heappop(heap)

        if curr_cost > dist[node]:
            continue

        if node == goal:
            break

        for neighbor, weight in undirected[node]:
            new_cost = curr_cost + weight

            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                parent[neighbor] = node
                heapq.heappush(heap, (new_cost, neighbor))

    # unreachable
    if dist[goal] == float('inf'):
        return ([], None)

    # rebuild path
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent.get(cur)
    path.reverse()

    return (path, dist[goal])
