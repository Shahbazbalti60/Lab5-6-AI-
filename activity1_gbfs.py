"""Lab 05 - Activity 1: Understanding the Effect of a Heuristic (Greedy Best-First Search)"""

# Graph represented using an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 7,
    'B': 5,
    'C': 3,
    'D': 4,
    'E': 2,
    'F': 1,
    'G': 0
}


def greedy_best_first(graph, heuristic, start, goal):
    # Frontier initially contains the start node
    frontier = [start]
    # Set to keep track of visited nodes
    visited = set()

    while frontier:
        # Select the node having the smallest heuristic
        current = min(frontier, key=lambda node: heuristic[node])
        frontier.remove(current)
        print(current)

        # Goal test
        if current == goal:
            print("Goal found!")
            return

        visited.add(current)

        # Add unvisited neighbours to the frontier
        for neighbour in graph[current]:
            if neighbour not in visited and neighbour not in frontier:
                frontier.append(neighbour)


# Driver Code
if __name__ == "__main__":
    greedy_best_first(graph, heuristic, 'A', 'G')
