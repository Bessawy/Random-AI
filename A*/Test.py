from queue import PriorityQueue
from math import inf


def astar(start_state, goaltest, h):
    """
    Perform A-star search.

    Finds a sequence of actions from `start_state` to some end state satisfying
    the `goaltest` function by performing A-star search.

    This function returns a policy, i.e. a sequence of actions which, if
    successively applied to `start_state` will transform it into a state which
    satisfies `goaltest`.

    Parameters
    ----------
    start_state : State
       State object with `successors` function.
    goaltest : Function (State -> bool)
       A function which takes a State object as parameter and returns True if
       the state is an acceptable goal state.
    h : Function (State -> float)
       Heuristic function estimating the distance from a state to the goal.
       This is the h(s) in f(s) = h(s) + g(s).

    Returns
    -------
    list of actions
       The policy for transforming start_state into one which is accepted by
       `goaltest`.
    """
    # Dictionary to look up predecessor states and the
    # the actions which took us there. It is empty to start with.
    predecessor = {}
    # Dictionary holding the (yet) best found distance to a state,
    # the function g(s) in the formula f(s) = h(s) + g(s).
    g = {}
    # Priority queue holding states to check, the priority of each state is
    # f(s).
    # Elements are encoded as pairs of (prio, state),
    # e.g. Q.put( (prio, state ))
    # And gotten as (prio,state) = Q.get()
    Q = PriorityQueue(maxsize=0)
    goal_state = None
    reached = False

    Best = inf
    g[start_state] = 0
    predecessor[start_state] = start_state

    Q.put((h(start_state), start_state))

    while not Q.empty():
        f , state = Q.get()

        if f < Best :
            for a,s in state.successors():
                if goaltest(s):
                    reached = True
                    goal_state = s

                    if s not in g:
                        g[s] = g[state] + a.cost
                        predecessor[s] = (state,a)
                    else:
                        if g[s] > g[state] + a.cost :
                            g[s] = g[state] + a.cost
                            predecessor[s] = (state,a)
                    Best = g[s]

                else:
                    if s not in g:
                        g[s] = g[state] + a.cost
                        predecessor[s] = (state,a)
                        Q.put((h(s) + g[s], s))

                    else:
                        if g[s] > g[state] + a.cost:
                            g[s] = g[state] + a.cost
                            predecessor[s] = (state, a)
                            Q.put((h(s) + g[s], s))


    if reached:
        actions = []
        current_state = goal_state
        while current_state != start_state:
            state, action = predecessor[current_state]
            actions.append(action)
            current_state = state

        actions.reverse()
        return actions
    else:
        return 0

    # TermTestState (see below) is designed so that the first solution found
    # has a higher cost than the second solution.
    # Start in stateindex 1 and look for path to index 0.


""" Tests for astar search."""

""" Tests for astar search."""

import unittest
import itertools
from action import Action
from state import State
from mappgridstate import MAPPGridState
from mappdistance import MAPPDistanceSum


class TestAstar(unittest.TestCase):
    """Tests for astar search method."""

    def setUp(self):
        self.mapp_1_s = MAPPGridState.create_from_string(["1..",
                                                          "...",
                                                          "..."])
        self.mapp_1_g = MAPPGridState.create_from_string(["...",
                                                          "...",
                                                          "..1"])


    def test_5_correctness(self):
        """The best solution (least cost) should be returned, not the first one."""
        # TermTestState (see below) is designed so that the first solution found
        # has a higher cost than the second solution.
        # Start in stateindex 1 and look for path to index 0.
        plan = list(astar(TermTestState(), lambda state: (state.state == 0),  # goal test
                          TermTestState.TermTestH))  # function: distance to goal

        correct = [Action("1", "3", cost=1.0),
                   Action("3", "4", cost=0.5),
                   Action("4", "5", cost=0.5),
                   Action("5", "6", cost=0.5),
                   Action("6", "G", cost=0.5)]

        cost = sum(p.cost for p in plan)
        c_cost = sum(c.cost for c in correct)
        # Check cost
        self.assertEqual(cost, c_cost,
                         f"Correct cost {c_cost}, your plan cost: {cost}. Check so you return the best solution, and not only the first one found if you have too high cost. Check so you return the full path if too low."
                         )
        # Check path in general.
        self.assertTrue(len(plan) == len(correct) and all(p == c for p, c in zip(plan, correct)),
                        f"Correct plan: {correct}; Your plan: {plan}; Make sure that the plan isn't e.g. reversed.")




class TermTestState(State):
    """
    State class designed to provide a higher cost path to goal first.
    """

    def __init__(self, stateindex=1):
        self.state = stateindex

    # Construct a string representing a state.
    def __repr__(self):
        return str(self.state)

    # The hash function for states, mapping each state to an integer
    def __hash__(self):
        return self.state

    # Equality of states.
    def __eq__(self, other):
        return (self.state == other.state)

    # queue.PriorityQueue needs an ordering of states
    def __lt__(self, other):
        return False

    # Compute all successors
    # 1 has 2, 3
    # 2 has 0 (the goal state)
    # 3 has 4
    # 4 has 5
    # 5 has 6
    # 6 has 0
    def successors(self):
        if self.state == 1:
            return [(Action("1", "2", 1.0), TermTestState(2)),
                    (Action("1", "3", 1.0), TermTestState(3))]
        elif self.state == 2:
            return [(Action("2", "G", 5.0), TermTestState(0))]
        elif self.state == 3:
            return [(Action("3", "4", 0.5), TermTestState(4))]
        elif self.state == 4:
            return [(Action("4", "5", 0.5), TermTestState(5))]
        elif self.state == 5:
            return [(Action("5", "6", 0.5), TermTestState(6))]
        elif self.state == 6:
            return [(Action("6", "G", 0.5), TermTestState(0))]
        elif self.state == 0:
            return []
        else:
            return 0.0

    # Create an h-function so that the path to 0 through 2
    # is found first, and the optimal path (which is longer)
    # is found later.
    # Static method in class.
    def TermTestH(s):
        if s.state == 0:
            return 0.0
        elif s.state == 1:
            return 2.0
        elif s.state == 2:
            return 1.0
        elif s.state == 3:
            return 2.0
        elif s.state == 4:
            return 1.5
        elif s.state == 5:
            return 1.0
        elif s.state == 6:
            return 0.5
        else:
            return 0.0


if __name__ == "__main__":
    unittest.main()
