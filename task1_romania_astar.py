"""Lab 06 - Graded Lab Task 1: A* search Arad -> Bucharest (Romania problem)
and comparison with uninformed methods (BFS, DFS, UCS) and Greedy Best-First."""
import heapq
from collections import deque

# Road distances (km)
roads = {
    ('Arad', 'Zerind'): 75, ('Arad', 'Sibiu'): 140, ('Arad', 'Timisoara'): 118,
    ('Zerind', 'Oradea'): 71, ('Oradea', 'Sibiu'): 151,
    ('Timisoara', 'Lugoj'): 111, ('Lugoj', 'Mehadia'): 70,
    ('Mehadia', 'Dobreta'): 75, ('Dobreta', 'Craiova'): 120,
    ('Sibiu', 'Fagaras'): 99, ('Sibiu', 'Rimnicu Vilcea'): 80,
    ('Rimnicu Vilcea', 'Craiova'): 146, ('Rimnicu Vilcea', 'Pitesti'): 97,
    ('Craiova', 'Pitesti'): 138, ('Fagaras', 'Bucharest'): 211,
    ('Pitesti', 'Bucharest'): 101, ('Bucharest', 'Giurgiu'): 90,
    ('Bucharest', 'Urziceni'): 85, ('Urziceni', 'Hirsova'): 98,
    ('Urziceni', 'Vaslui'): 142, ('Hirsova', 'Eforie'): 86,
    ('Vaslui', 'Iasi'): 92, ('Iasi', 'Neamt'): 87,
}

graph = {}
for (a, b), d in roads.items():
    graph.setdefault(a, []).append((b, d))
    graph.setdefault(b, []).append((a, d))

# Straight-line distance to Bucharest (heuristic)
h_sld = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242, 'Eforie': 161,
    'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
    'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100,
    'Rimnicu Vilcea': 193, 'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80,
    'Vaslui': 199, 'Zerind': 374,
}


def path_cost(path):
    return sum(dict(graph[a])[b] for a, b in zip(path, path[1:]))


def build_path(parent, node):
    path = []
    while node is not None:
        path.append(node)
        node = parent[node]
    return path[::-1]


# ------------------------------------------------------------------ A*
def a_star(start, goal, verbose=True):
    open_list = [(h_sld[start], 0, start)]          # (f, g, node)
    g_cost = {start: 0}
    parent = {start: None}
    closed = set()
    expanded = []
    if verbose:
        print(f"{'Expanded node':<16}{'g':>5}{'h':>6}{'f':>6}")
    while open_list:
        f, g, node = heapq.heappop(open_list)
        if node in closed:
            continue
        expanded.append(node)
        if verbose:
            print(f"{node:<16}{g:>5}{h_sld[node]:>6}{f:>6}")
        if node == goal:
            p = build_path(parent, node)
            return p, g, expanded
        closed.add(node)
        for nb, d in graph[node]:
            ng = g + d
            if nb not in g_cost or ng < g_cost[nb]:
                g_cost[nb] = ng
                parent[nb] = node
                heapq.heappush(open_list, (ng + h_sld[nb], ng, nb))
    return None, None, expanded


# ------------------------------------------------------- uninformed / other
def bfs(start, goal):
    frontier = deque([start])
    parent = {start: None}
    expanded = []
    while frontier:
        node = frontier.popleft()
        expanded.append(node)
        if node == goal:
            p = build_path(parent, node)
            return p, path_cost(p), expanded
        for nb, _ in graph[node]:
            if nb not in parent:
                parent[nb] = node
                frontier.append(nb)
    return None, None, expanded


def dfs(start, goal):
    frontier = [start]
    parent = {start: None}
    visited = set()
    expanded = []
    while frontier:
        node = frontier.pop()
        if node in visited:
            continue
        visited.add(node)
        expanded.append(node)
        if node == goal:
            p = build_path(parent, node)
            return p, path_cost(p), expanded
        for nb, _ in reversed(graph[node]):
            if nb not in visited:
                parent[nb] = node
                frontier.append(nb)
    return None, None, expanded


def ucs(start, goal):
    open_list = [(0, start)]
    g_cost = {start: 0}
    parent = {start: None}
    closed = set()
    expanded = []
    while open_list:
        g, node = heapq.heappop(open_list)
        if node in closed:
            continue
        expanded.append(node)
        if node == goal:
            return build_path(parent, node), g, expanded
        closed.add(node)
        for nb, d in graph[node]:
            ng = g + d
            if nb not in g_cost or ng < g_cost[nb]:
                g_cost[nb] = ng
                parent[nb] = node
                heapq.heappush(open_list, (ng, nb))
    return None, None, expanded


def greedy(start, goal):
    open_list = [(h_sld[start], start)]
    parent = {start: None}
    visited = set()
    expanded = []
    while open_list:
        _, node = heapq.heappop(open_list)
        if node in visited:
            continue
        visited.add(node)
        expanded.append(node)
        if node == goal:
            p = build_path(parent, node)
            return p, path_cost(p), expanded
        for nb, _ in graph[node]:
            if nb not in parent:
                parent[nb] = node
                heapq.heappush(open_list, (h_sld[nb], nb))
    return None, None, expanded


if __name__ == "__main__":
    start, goal = 'Arad', 'Bucharest'

    print("=" * 60)
    print("A* SEARCH:", start, "->", goal)
    print("=" * 60)
    path, cost, expanded = a_star(start, goal)
    print("\nPath      :", " -> ".join(path))
    print("Total cost:", cost, "km")
    print("Nodes expanded:", len(expanded))

    print("\n" + "=" * 60)
    print("COMPARISON WITH OTHER SEARCH METHODS")
    print("=" * 60)
    results = [
        ("BFS (uninformed)", bfs(start, goal)),
        ("DFS (uninformed)", dfs(start, goal)),
        ("UCS (uninformed)", ucs(start, goal)),
        ("Greedy Best-First (informed)", greedy(start, goal)),
        ("A* (informed)", (path, cost, expanded)),
    ]
    print(f"{'Algorithm':<30}{'Nodes expanded':>15}{'Cost (km)':>11}  Path")
    print("-" * 100)
    for name, (p, c, e) in results:
        print(f"{name:<30}{len(e):>15}{c:>11}  {' -> '.join(p)}")

    print("\nObservations:")
    print("* A* found the optimal route (418 km) after expanding only 6 nodes, while")
    print("  UCS needed 13 and BFS needed 9 to reach the same goal.")
    print("* DFS also expanded 6 nodes, but its route is much longer (607 km) -- it")
    print("  got lucky on node count, not on quality. BFS ignores road distances and")
    print("  returns the fewest-hops route (450 km), which is not the cheapest.")
    print("* Greedy Best-First is the fastest (4 nodes) but only follows h(n), so it")
    print("  returns a sub-optimal 450 km route. A* combines g(n)+h(n) and gets both")
    print("  a small search effort AND the optimal answer.")
    print("* UCS is optimal too, but without a heuristic it expands every city cheaper")
    print("  than 418 km in all directions (including Zerind, Timisoara, ...).")
