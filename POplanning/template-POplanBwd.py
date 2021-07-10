
from plans import PlanNode, PlanEmpty

#
# Find a plan that solves a partially observable planning problem.
#

# Compute the strong preimage of a state set

def strongpreimage(bstate,action):
    result = set()
    for s in bstate:
        for s2 in s.preds(action):
            if s2.succs(action).issubset(bstate):
                result.add(s2)
    return result

# Construct a branching plan for a problem instance with partial observability.

def POsolver(instance):

    initialStates, goalStates,allActions = instance

    P = [ (PlanEmpty(),goalStates) ]

    while True:
        plan,bstate = backup(P,allActions)
        if plan == None:
            return None

        # A state set that covers all initial states: plan has been found

        if initialStates.issubset(bstate):
            return plan
        oldP = P
        P = [ (p,b) for p,b in oldP if not b.issubset(bstate) ]
        P.append( (plan,bstate) )

        print("New with depth " + str(plan.plandepth()) + " size " + str(plan.plansize()) + " states " + str(len(bstate)) + ": total " + str(len(P)) + " plans/belief states")

# Backup operation for discrete belief states

# The backup operation: Find a state set for which no plan existed before
#
# This can be implemented as follows.
#
# Try out every action, and see if for every observation for that
# action we can find an existing plan so that the new plan
# works for a state set for which no plan has existed before.
# Trying out every action can be done with a loop.

# Trying out all combinations of observation + sub-plan is best done
# with e recursive procedure that handles each observation for the
# action in one recursive call, trying out all sub-plans for that
# observation one at a time, followed by a recursive call to
# the same procedure for handling the next and subsequent
# observations.

# The base case of the recursive procedure computes the preimage
# of the union of all of the state sets for the observations,
# and checks whether a state set for which no plan existed before
# was found. If not, backtracking through the tree continues.
#
# The all the combinations of observation - sub-plan can
# be depicted as the following tree, which also illustrates
# the structure of the recursive procedure calls
#
#
# observation 1     observation 2    observation 3
#                    
#                    
#                / sub-plan 2.1 ..   / sub-plan 3.1
#               /                   /
#              /                   /
#  sub-plan 1.1 -- sub-plan 2.2 ------ sub-plan 3.2
#              \                   \
#               \                   \
#                \ sub-plan 2.3 ..   \ sub-plan 3.3
#
#  sub-plan 1.2 ..
#
#  sub-plan 1.3 ..
#
#  ...



def backup(P,allActions):
    for a in allActions:


    pass
###
###
###
###
###
###
###
