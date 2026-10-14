"""Lab 05 - Graded Task 2: Solve the 8-Puzzle using Greedy Best-First Search
Heuristic: h(n) = number of misplaced tiles (blank is not counted)."""

import heapq

START = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)          # 0 = blank
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def h(state):
    """Number of misplaced tiles (blank excluded)."""
    return sum(1 for i, t in enumerate(state) if t != 0 and t != GOAL[i])


def get_neighbours(state):
    """All states reachable by moving the blank up/down/left/right."""
    i = state.index(0)
    r, c = divmod(i, 3)
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr * 3 + nc
            s = list(state)
            s[i], s[j] = s[j], s[i]
            yield tuple(s)


def print_state(state):
    for r in range(3):
        print("   " + " ".join(str(t) if t != 0 else "_" for t in state[3 * r:3 * r + 3]))


def greedy_best_first(start, goal):
    counter = 0                       # tie-breaker so heap never compares tuples of states
    frontier = [(h(start), counter, start)]
    parent = {start: None}
    visited = set()
    explored = 0

    while frontier:
        hv, _, current = heapq.heappop(frontier)
        if current in visited:
            continue
        visited.add(current)
        explored += 1

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1], explored

        for nb in get_neighbours(current):
            if nb not in parent:
                parent[nb] = current
                counter += 1
                heapq.heappush(frontier, (h(nb), counter, nb))
    return None, explored


if __name__ == "__main__":
    path, explored = greedy_best_first(START, GOAL)
    if path is None:
        print("No solution found.")
    else:
        print("Sequence of states from start to goal:\n")
        for step, state in enumerate(path):
            label = "Initial state" if step == 0 else f"Step {step}"
            print(f"{label}  (h = {h(state)})")
            print_state(state)
            print()
        print("Total number of steps in the solution:", len(path) - 1)
        print("Total number of states explored      :", explored)
