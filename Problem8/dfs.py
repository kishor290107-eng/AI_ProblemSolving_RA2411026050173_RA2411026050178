graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()

    path = path + [start]

    if start == goal:
        return path

    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path, visited)
            if result:
                return result

    return None


if __name__ == "__main__":
    start = input("Enter start node: ")
    goal = input("Enter goal node: ")

    result = dfs(graph, start, goal)

    if result:
        print("DFS Path:", result)
    else:
        print("No path found")
