import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 0
}

def astar(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor, cost in graph[current]:
            new_cost = g_cost[current] + cost

            if new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(open_list, (priority, neighbor))
                came_from[neighbor] = current

    return None


if __name__ == "__main__":
    start = input("Enter start node: ")
    goal = input("Enter goal node: ")

    path = astar(graph, heuristic, start, goal)

    if path:
        total_cost = 0
        for i in range(len(path) - 1):
            for neighbor, cost in graph[path[i]]:
                if neighbor == path[i+1]:
                    total_cost += cost

        print("A* Path:", path)
        print("Total Cost:", total_cost)
    else:
        print("No path found")
