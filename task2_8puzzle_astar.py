"""Lab 06 - Graded Lab Task 2: 8-Puzzle using A* Search
f(n) = g(n) + h(n), g = number of moves (each move costs 1),
h = number of misplaced tiles (blank not counted)."""
import heapq

START = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)          # 0 = blank
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def h(state):
    return sum(1 for i, t in enumerate(state) if t != 0 and t != GOAL[i])


def count_inversions(state):
    tiles = [t for t in state if t != 0]
    return sum(1 for i in range(len(tiles)) for j in range(i + 1, len(tiles))
               if tiles[i] > tiles[j])


def get_neighbours(state):
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


def a_star(start, goal):
    counter = 0
    open_list = [(h(start), counter, 0, start)]       # (f, tie, g, state)
    g_cost = {start: 0}
    parent = {start: None}
    closed = set()
    expanded = 0

    while open_list:
        f, _, g, current = heapq.heappop(open_list)
        if current in closed:
            continue
        closed.add(current)
        expanded += 1

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1], expanded

        for nb in get_neighbours(current):
            ng = g + 1                                   # unit cost per tile move
            if nb not in g_cost or ng < g_cost[nb]:
                g_cost[nb] = ng
                parent[nb] = current
                counter += 1
                heapq.heappush(open_list, (ng + h(nb), counter, ng, nb))
    return None, expanded


if __name__ == "__main__":
    if count_inversions(START) % 2 != 0:
        print("This start state is not solvable.")
    else:
        path, expanded = a_star(START, GOAL)
        print("Sequence of states from start to goal:\n")
        for g, state in enumerate(path):
            label = "Initial state" if g == 0 else f"Step {g}"
            print(f"{label}  (g = {g}, h = {h(state)}, f = {g + h(state)})")
            print_state(state)
            print()
        print("Total number of steps (path cost):", len(path) - 1)
        print("Total number of states expanded  :", expanded)
