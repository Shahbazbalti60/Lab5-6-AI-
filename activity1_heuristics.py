"""Lab 06 - Activity 1: Understanding Heuristics for A* Search"""
import math


def manhattan_distance(current, goal):
    """4-directional movement (up, down, left, right)."""
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


def diagonal_distance(current, goal):
    """8-directional movement, every move has unit cost."""
    dx = abs(current[0] - goal[0])
    dy = abs(current[1] - goal[1])
    return max(dx, dy)


def euclidean_distance(current, goal):
    """Straight-line distance."""
    return math.sqrt((goal[0] - current[0]) ** 2 + (goal[1] - current[1]) ** 2)


current = (1, 1)
goal = (4, 8)

print("Current =", current, " Goal =", goal)
print("Manhattan distance :", manhattan_distance(current, goal))
print("Diagonal distance  :", diagonal_distance(current, goal))
print("Euclidean distance :", euclidean_distance(current, goal))
