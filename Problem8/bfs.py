from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None


if __name__ == "__main__":
    start = input("Enter start node: ")
    goal = input("Enter goal node: ")

    result = bfs(graph, start, goal)

    if result:
        print("BFS Path:", result)
    else:
        print("No path found")
