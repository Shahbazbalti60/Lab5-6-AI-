LAB 05 (GBFS) and LAB 06 (A*) - SOLUTIONS
=========================================
Requirements: Python 3.8+ (no extra libraries needed).

HOW TO RUN (open a terminal inside this folder):

Lab 05
  python lab05_GBFS/activity1_gbfs.py
  python lab05_GBFS/activity2_gbfs_new_heuristic.py
  python lab05_GBFS/task1_manhattan.py            <- Graded Task 1
  python lab05_GBFS/task2_8puzzle_gbfs.py         <- Graded Task 2
  python lab05_GBFS/task3_8puzzle_user_input.py   <- Graded Task 3 (interactive)

Lab 06
  python lab06_AStar/activity1_heuristics.py
  python lab06_AStar/activity2_maze_astar.py
  python lab06_AStar/task1_romania_astar.py       <- Lab Task 1
  python lab06_AStar/task2_8puzzle_astar.py       <- Lab Task 2
  python lab06_AStar/task3_robot_maze_astar.py    <- Lab Task 3

(Use "python3" instead of "python" on Mac/Linux.)

NOTES
- Lab05 Task 3 asks for the 9 tiles typed row by row, 0 = blank.
  Press Enter for a default puzzle. Try "1 2 3 4 5 6 8 7 0" to see the
  "not solvable" message (odd number of inversions).
- Lab06 Task 1: the manual's table shows Pitesti = "10" (cut off in the
  image); the standard textbook value 100 is used.
- Lab06 Task 3: the maze was transcribed from the figure in the manual
  (9 rows x 10 columns). Coordinates are (row, column) from the top-left.
