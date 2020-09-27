import search as s               # from AIMA code

class WJ3(s.Problem):
    
    def __init__(self, capacities=(12,8,5), initial=(12,0,0), goal=(6,6,0)):
        self.capacities = capacities
        self.initial = initial
        self.goal = goal

    def __repr__(self):
        """ Returns a string representing the object """
        return f"WJ3({self.capacities},{self.initial},{self.goal})"

    def goal_test(self, state):
        """ Returns True iff state is a goal state """
        G1, G2, G3 = self.goal
        return (state[0] == G1 or G1 < 0) and (state[1] == G2 or G2 < 0) and (state[2] == G3 or G3 < 0)
               
    def h(self, node):
        """ Estimate of cost of shortest path from node to a goal """
        i = 0
        difference = 0
        while i < len(node.state):
            difference += self.goal[i] - node.state[i]
            i += 1
        return 0 if self.goal_test(node.state) else abs(difference)

    def actions(self, state):
        """ generates legal actions for state """
        (J1, J2, J3) = state
        (C1, C2, C3) = self.capacities
        legal = []        
        if J3<C3: legal.append(('fetch', 3))
        if J1>0: legal.append(('dump', 1))
        if J2>0: legal.append(('dump', 2))
        if J3>0: legal.append(('dump', 3))        
        if J1<C1: legal.append(('fetch', 1))
        if J2<C2: legal.append(('fetch', 2))
        if J1<C1 and J2>0: legal.append(('pour', 2, 1))
        if J3<C3 and J2>0: legal.append(('pour', 2, 3))
        if J1<C1 and J3>0: legal.append(('pour', 3, 1))
        if J2<C2 and J3>0: legal.append(('pour', 3, 2))
        if J2<C2 and J1>0: legal.append(('pour', 1, 2))
        if J3<C3 and J1>0: legal.append(('pour', 1, 3))
        return legal

    def result(self, state, action):
        """ Returns the successor of state after doing action """
        #print(f"Calling result({state},{action}")        
        if len(action) == 2:
            act, arg1 = action
        elif len(action) == 3:
            act, arg1, arg2 = action
        else:
            raise ValueError(f"Bad action: {action}")

        (J1, J2, J3) = state
        (C1, C2, C3) = self.capacities
        
        if act == 'fetch':
            if arg1 == 1:
                J1 = C1
                return (J1,J2,J3)
            elif arg1 == 2:
                J2 = C2
                return (J1,J2,J3)                
            else:
                J3 = C3
                return (J1,J2,J3)       
        elif act == 'dump':
            if arg1 == 1:
                return (0, J2, J3)
            elif arg1 == 2:
                return (J1, 0, J3)
            else:
                return (J1, J2, 0)
        elif act == 'pour':
            if arg1 == 1 and arg2 == 2: 
                delta = min(J1, C2-J2)
                return (J1-delta, J2+delta, J3)
            elif arg1 == 1 and arg2 == 3: 
                delta = min(J1, C3-J3)
                return (J1-delta, J2, J3+delta)
            elif arg1 == 2 and arg2 == 1: 
                delta = min(J2, C1-J1)
                return (J1+delta, J2-delta, J3)
            elif arg1 == 2 and arg2 == 3: 
                delta = min(J2, C3-J3)
                return (J1, J2-delta, J3+delta)
            elif arg1 == 3 and arg2 == 1:     
                delta = min(J3, C1-J1)
                return (J1+delta, J2, J3-delta)
            elif arg1 == 3 and arg2 == 2:     
                delta = min(J3, C1-J1)
                return (J1+delta, J2, J3-delta)
            else:
                raise ValueError(f"Bad action: {action}")
        else:
            raise ValueError(f"Bad action: {action}")

  
    def reachable_states(self):
        fringe = set({(self.initial)})
        seen = set()
        while fringe != set():
            temp = fringe.pop()
            seen.add(temp)
            acts = self.actions(temp)
            for act in acts:
                successor = self.result(temp, act)
                if successor not in seen:
                    fringe.add(successor)
        return seen

    def path_cost(self, c, state1, action, state2):
            """ Cost of path from start node to state1 assuming cost c to
            get to state1 and doing action to get to state2 """
            (J1, J2, J3) = state1
            (C1, C2, C3) = self.capacities
            if action[0] == 'fetch':
                if action[0] == 1:
                    fill = C1-J1
                    return c + fill + 1
                elif action[1] == 2:
                    fill = C2-J2
                    return c + fill + 1
                else:
                    fill = C3-J3
                    return c+ fill + 1
            else:
                return c + 1


def print_solution(solution):
    """If a path to a goal was found, prints the cost and the sequence of actions
    and states on a path from the initial state to the goal found"""
    if not solution:
        print("No solution found 🙁")
    else:
        print("Path of cost", solution.path_cost, end=': ')
        for node in solution.path():
            if not node.action:
                print(node.state, end=' ')
            else:
                 print(f'-{node.action}->{node.state}', end=' ')