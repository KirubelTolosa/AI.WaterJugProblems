##Q1.
Upper Bound = (C1 + 1) * (C2 + 1) * (C3 + 1)
P1(1, 1, 1) :  8
P2((1, 1, 1) : 8
P3((1, 1, 1) : 8
P4((2, 2, 2) : 27
P5((5, 2, 0) : 18
P6((5, 2, 0) : 18
P7((5, 3, 3 : 96
P8((4, 3, 2) : 60
P9((12, 8, 5) : 702

##Q2.
The BFS algorithm is not the most feasible algorithm for this problem as the problem has highest numbers of possible states/successors and actions compared to the other problems. This is because BFS finds an optimal solution with a minimal number of actions. In addition, not all actions in our solution cost the same, which also makes using BFS to solve this problem rather costly because BFS traverses through every node accross a level untill it reaches the goal state. The high number of the capacities give this problem a higher depth and breadth compared to the others and BFS traverses through the entire breadth of the tree at each depth to the goal, making it not the ideal algorithm for this particular problem.  I believe IDDFS may not help much, or is probably an overlaod as the goal node is found deep down the tree of the possible states in the problem.

##Q3.
My heuristic returns 0 if it is the goal state or the absolute difference of between the values of the current node and goal node. The heuristic will always be admissible as stays equal to the difference between the current state and goal state. We can also consider it consistent as returns a consistent estimate for every node. The solution greately improves the A* algorithm tests. 