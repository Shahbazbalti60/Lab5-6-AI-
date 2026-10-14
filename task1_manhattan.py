"""Lab 05 - Graded Task 1: Manhattan Distance as a Heuristic"""


def manhattan_distance(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


goal = (4, 4)
positions = [(0, 0), (1, 2), (2, 3), (3, 4), (4, 4)]

print("Goal =", goal)
print("-" * 45)
print(f"{'Position':<12}{'Calculation':<22}{'h(n)':>5}")
print("-" * 45)
for pos in positions:
    calc = f"|{goal[0]}-{pos[0]}| + |{goal[1]}-{pos[1]}|"
    print(f"{str(pos):<12}{calc:<22}{manhattan_distance(pos, goal):>5}")
print("-" * 45)

best = min(positions, key=lambda p: manhattan_distance(p, goal))
print("Closest position to the goal:", best)
