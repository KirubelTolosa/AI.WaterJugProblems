import wj3
import search as s
from wj3test_problems import tests

# default searchers from aima.search to use
default_searchers = [s.breadth_first_graph_search,
                     s.depth_first_graph_search,
                     s.astar_search]

def wj3solve(capacities, start, goal, searchers=default_searchers):
    problem = wj3.WJ3(capacities, start, goal)
    print(f"Solving {problem}\n")
    reachable = problem.reachable_states()
    potential = (capacities[0]+1) * (capacities[1]+1) * (capacities[2]+1)
    print(f"{len(reachable)} of {potential} reachable states: {reachable}\n")
    successful_searchers = []
    print('searchers', [s.__name__ for s in searchers])
    for alg in searchers:
        print(f"• {alg.__name__}", end=': ')
        solution = alg(problem)
        if solution:
            wj3.print_solution(solution)
            successful_searchers.append(alg)
        print()
    print("\nSUMMARY: algorithm  <successors  goal_tests  states_generated  solution>")
    if successful_searchers:
        s.compare_searchers([problem], [], searchers=successful_searchers)

def solve_all(plist):
    for capacities, start, goal in plist:
        print('**********************************************************************')
        try:
            wj3solve(capacities, start, goal)
        except Exception as e:
            print(f'*** ERROR {e} **')
        print()

def firstN(arg, n):
    arglist = list(arg)[:n]
    arglist.append('...')
    return arglist

solve_all(tests)