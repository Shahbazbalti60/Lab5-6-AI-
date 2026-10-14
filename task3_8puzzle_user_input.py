"""Lab 05 - Graded Task 3: 8-Puzzle with user input + solvability check + GBFS

Solvability rule (3x3 puzzle, odd grid width):
  Write the tiles in row order ignoring the blank. Count 'inversions' = pairs of
  tiles (a, b) where a appears before b but a > b.
  If the number of inversions is EVEN  -> the puzzle is solvable.
  If it is ODD                         -> the puzzle is NOT solvable.
(The goal state 1 2 3 4 5 6 7 8 _ has 0 inversions, and every legal move
preserves the parity of the inversion count.)
"""

import heapq

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)
DEFAULT = "8 1 3 4 0 2 7 6 5"      # used when the user just presses Enter


def h(state):
    return sum(1 for i, t in enumerate(state) if t != 0 and t != GOAL[i])


def count_inversions(state):
    tiles = [t for t in state if t != 0]
    return sum(1 for i in range(len(tiles)) for j in range(i + 1, len(tiles))
               if tiles[i] > tiles[j])


def is_solvable(state):
    return count_inversions(state) % 2 == 0


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


def greedy_best_first(start, goal):
    counter = 0
    frontier = [(h(start), counter, start)]
    parent = {start: None}
    visited = set()
    explored = 0
    while frontier:
        _, _, current = heapq.heappop(frontier)
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


def read_state():
    print("Enter the 9 values of the start state row by row, separated by spaces.")
    print("Use 0 for the blank.  Example: 1 2 3 4 0 6 7 5 8")
    print(f"(Press Enter to use the default: {DEFAULT})")
    while True:
        raw = input("Start state: ").strip() or DEFAULT
        try:
            values = tuple(int(x) for x in raw.replace(",", " ").split())
        except ValueError:
            print("  Please enter numbers only.")
            continue
        if sorted(values) != list(range(9)):
            print("  Invalid input: use each number 0-8 exactly once (9 values).")
            continue
        return values


def solve_once():
    start = read_state()
    print("\nGoal state:")
    print_state(GOAL)
    print("\nStart state:")
    print_state(start)

    inv = count_inversions(start)
    print(f"\nNumber of inversions = {inv}")
    if not is_solvable(start):
        print("Inversions are ODD -> this puzzle is NOT solvable. Search skipped.")
        return
    print("Inversions are EVEN -> this puzzle IS solvable. Running GBFS...\n")

    path, explored = greedy_best_first(start, GOAL)
    for step, state in enumerate(path):
        label = "Initial state" if step == 0 else f"Step {step}"
        print(f"{label}  (h = {h(state)})")
        print_state(state)
        print()
    print("Total number of steps in the solution:", len(path) - 1)
    print("Total number of states explored      :", explored)


if __name__ == "__main__":
    while True:
        solve_once()
        again = input("\nTry another puzzle? (y/n): ").strip().lower()
        if again != "y":
            break
        print()
