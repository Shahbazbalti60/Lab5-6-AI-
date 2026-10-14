"""Lab 06 - Activity 2: Maze Path Planning Using A* Search (Manhattan heuristic)"""
import heapq

# Coordinates of traversable nodes
nodes = {
    'A': (0, 0), 'B': (2, 0), 'C': (3, 0), 'D': (4, 0), 'E': (5, 0),
    'F': (0, 1), 'G': (2, 1),
    'H': (0, 2), 'I': (1, 2), 'J': (2, 2), 'K': (4, 2), 'L': (5, 2),
    'M': (0, 3), 'N': (1, 3), 'O': (3, 3), 'P': (4, 3), 'Q': (5, 3),
    'R': (0, 4), 'S': (1, 4), 'T': (2, 4), 'U': (3, 4), 'V': (5, 4),
    'W': (2, 5), 'X': (4, 5), 'Y': (5, 5)
}

# Graph connections based on valid up/down/left/right moves
graph = {
    'A': ['F'],
    'B': ['C', 'G'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['D'],
    'F': ['A', 'H'],
    'G': ['B', 'J'],
    'H': ['F', 'I', 'M'],
    'I': ['H', 'J', 'N'],
    'J': ['I', 'G'],
    'K': ['L', 'P'],
    'L': ['K', 'Q'],
    'M': ['H', 'N', 'R'],
    'N': ['M', 'I', 'S'],
    'O': ['P', 'U'],
    'P': ['O', 'Q', 'K'],
    'Q': ['P', 'L', 'V'],
    'R': ['M', 'S'],
    'S': ['R', 'T', 'N'],
    'T': ['S', 'U', 'W'],
    'U': ['T', 'O'],
    'V': ['Q', 'Y'],
    'W': ['T'],
    'X': [],
    'Y': ['V']
}


def manhattan_distance(node, goal):
    x1, y1 = nodes[node]
    x2, y2 = nodes[goal]
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(graph, start, goal):
    open_list = []
    # (f-value, node)
    heapq.heappush(open_list, (manhattan_distance(start, goal), start))

    g_cost = {start: 0}
    parent = {start: None}
    closed = set()

    while open_list:
        current_f, current = heapq.heappop(open_list)

        if current in closed:
            continue

        print("Node:", current,
              "g =", g_cost[current],
              "h =", manhattan_distance(current, goal),
              "f =", current_f)

        # Goal test
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        closed.add(current)

        # Explore neighbours
        for neighbour in graph[current]:
            new_g = g_cost[current] + 1
            if neighbour not in g_cost or new_g < g_cost[neighbour]:
                g_cost[neighbour] = new_g
                h = manhattan_distance(neighbour, goal)
                f = new_g + h
                parent[neighbour] = current
                heapq.heappush(open_list, (f, neighbour))

    return None


# Driver code
if __name__ == "__main__":
    start = 'A'
    goal = 'Y'
    path = a_star(graph, start, goal)

    print("\nFinal Path:")
    print(path)

    if path:
        print("Total Path Cost:", len(path) - 1)
    else:
        print("No path found.")
