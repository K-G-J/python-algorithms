"""
You can use a graph search algorithm to traverse the entirety of a graph data structure to locate a specific value

Vertices in a graph search include a “visited” list to keep track of whether or not each vertex has been checked

Depth-first search (DFS) and breadth-first search (BFS) are two common approaches to graph search

The runtime for graph search algorithms is O(vertices + edges)

DFS, which employs either recursion or a stack data structure, is useful for determining whether a path exists between two points

BFS, which generally relies on a queue data structure, is helpful in finding the shortest path between two points

There are three common traversal orders which you can apply with DFS to generate a list of all values in a graph: pre-order, post-order, and reverse post-order
"""


def dfs(graph, current_vertex, target_value, visited=None):
    if visited is None:
        visited = []
    visited.append(current_vertex)
    if current_vertex is target_value:
        return visited

    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
            path = dfs(graph, neighbor, target_value, visited)
            if path:
                return path


def bfs(graph, start_vertex, target_value):
    path = [start_vertex]
    vertex_and_path = [start_vertex, path]
    bfs_queue = [vertex_and_path]
    visited = set()
    while bfs_queue:
        current_vertex, path = bfs_queue.pop(0)
        visited.add(current_vertex)
        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                if neighbor is target_value:
                    return path + [neighbor]
                else:
                    bfs_queue.append([neighbor, path + [neighbor]])


some_hazardous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['piranhas', 'bees']),
    'piranhas': set(['bees']),
    'bees': set(['lasers']),
    'lasers': set([])
}

print(bfs(some_hazardous_graph, 'sharks', 'bees'))
print(dfs(some_hazardous_graph, 'sharks', 'bees'))
