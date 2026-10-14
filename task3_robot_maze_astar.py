"""Lab 06 - Graded Lab Task 3: Robot maze solved with A* Search

The maze is read from the figure in the lab manual (9 rows x 10 columns).
  '#' = wall (black)   '.' = free cell (white)   'S' = start (red)   'G' = goal (green)
Coordinates are written as (row, column) with (0, 0) at the top-left corner.

The robot can face N/E/S/W and move forward any distance, stopping before a wall.
Every cell moved through costs 1, so the path cost = number of cells travelled.
Heuristic: Manhattan distance (4-directional movement, admissible & consistent).
"""
import heapq

MAZE = [
    "S...#.....",
    "..#...##..",
    "...#..##.#",
    ".#..#...##",
    ".##.......",
    ".#..###.##",
    "#..###....",
    ".###......",
    "...#......",
    "#.###...#G",
]

ROWS, COLS = len(MAZE), len(MAZE[0])
DIRS = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}


def find(ch):
    for r in range(ROWS):
        for c in range(COLS):
            if MAZE[r][c] == ch:
                return (r, c)


def free(r, c):
    return 0 <= r < ROWS and 0 <= c < COLS and MAZE[r][c] != '#'


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(start, goal):
    open_list = [(manhattan(start, goal), 0, start)]
    g_cost = {start: 0}
    parent = {start: None}
    closed = set()
    expanded = 0
    while open_list:
        f, g, cur = heapq.heappop(open_list)
        if cur in closed:
            continue
        closed.add(cur)
        expanded += 1
        if cur == goal:
            path = []
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            return path[::-1], g, expanded
        for dr, dc in DIRS.values():
            nb = (cur[0] + dr, cur[1] + dc)
            if free(*nb):
                ng = g + 1
                if nb not in g_cost or ng < g_cost[nb]:
                    g_cost[nb] = ng
                    parent[nb] = cur
                    heapq.heappush(open_list, (ng + manhattan(nb, goal), ng, nb))
    return None, None, expanded


def to_robot_commands(path):
    """Compress the cell path into 'face direction + move forward k cells' commands."""
    names = {v: k for k, v in DIRS.items()}
    cmds = []
    for a, b in zip(path, path[1:]):
        d = names[(b[0] - a[0], b[1] - a[1])]
        if cmds and cmds[-1][0] == d:
            cmds[-1][1] += 1
        else:
            cmds.append([d, 1])
    return cmds


def draw(path):
    on_path = set(path)
    print("   " + " ".join(str(c) for c in range(COLS)))
    for r in range(ROWS):
        row = []
        for c in range(COLS):
            ch = MAZE[r][c]
            if ch == '.' and (r, c) in on_path:
                ch = '*'
            row.append(ch)
        print(f"{r}  " + " ".join(row))


if __name__ == "__main__":
    start, goal = find('S'), find('G')
    print("Maze (# wall, S start, G goal, * path):\n")
    path, cost, expanded = a_star(start, goal)
    if path is None:
        print("No path found.")
    else:
        draw(path)
        print("\nStart:", start, " Goal:", goal)
        print("\nPath followed (row, col):")
        print(" -> ".join(str(p) for p in path))
        print("\nRobot commands (face a direction, then move forward):")
        for d, k in to_robot_commands(path):
            print(f"  Face {d}, move forward {k}")
        print("\nTotal path cost (cells travelled):", cost)
        print("Number of moves/turn commands    :", len(to_robot_commands(path)))
        print("Nodes expanded by A*             :", expanded)
