"""Lab 05 - Activity 2: Effect of Changing the Heuristic Function
Same graph as Activity 1, but with different heuristic values."""

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

old_heuristic = {'A': 7, 'B': 5, 'C': 3, 'D': 4, 'E': 2, 'F': 1, 'G': 0}
new_heuristic = {'A': 7, 'B': 2, 'C': 5, 'D': 1, 'E': 3, 'F': 2, 'G': 0}


def greedy_best_first(graph, heuristic, start, goal):
    frontier = [start]
    visited = set()
    order = []

    while frontier:
        current = min(frontier, key=lambda node: heuristic[node])
        frontier.remove(current)
        order.append(current)
        print(current)

        if current == goal:
            print("Goal found!")
            return order

        visited.add(current)
        for neighbour in graph[current]:
            if neighbour not in visited and neighbour not in frontier:
                frontier.append(neighbour)
    return order


if __name__ == "__main__":
    print("=== Old heuristic (Activity 1) ===")
    old_order = greedy_best_first(graph, old_heuristic, 'A', 'G')

    print("\n=== New heuristic (Activity 2) ===")
    new_order = greedy_best_first(graph, new_heuristic, 'A', 'G')

    print("\nComparison")
    print("Old traversal:", " -> ".join(old_order))
    print("New traversal:", " -> ".join(new_order))
    print("\nThe graph is identical, but the changed heuristic values changed the")
    print("search direction (C/F branch before, B/D branch now).")
