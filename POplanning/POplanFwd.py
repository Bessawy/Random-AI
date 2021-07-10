
from plans import PlanNode, PlanEmpty

#
# Find a plan that solves a partially observable planning problem
#

# Identify all actions applicable in a state set.
# This is the intersection of the sets of actions
# applicable in each state.

def Bapplicable(bstate0):
    bstate = bstate0.copy()
    s = bstate.pop()
    actions = s.applActions()
    def inall(a):
        for s2 in bstate:
            if not a in s2.applActions():
                return False
        return True
    return [ a for a in actions if inall(a) ]

# Compute the successor state set w.r.t. a given action.

def Bsucc(bstate,action):
    result = set()
    for s in bstate:
#        print(s)
        result.update(s.succs(action))
    return result

# Return the subset of states compatible with the observation.
def Bobserve(bstate,observation):
    return { s for s in bstate if s.compatible(observation) }

# Construct a branching plan for a problem instance with partial observability.
# brute force


def GOforward(bstate,  goal, P):

    if bstate in P:
        return False, None

    if bstate.issubset(goal):
        return True, [PlanEmpty()]

    actions = Bapplicable(bstate)

    Policy = []
    trigger = False

    for a in actions:
        #print(str(a))
        lis = []
        nstate = Bsucc(bstate, a)
        observs = a.observations()

        for observ in observs:
            states = Bobserve(nstate, observ)
            status, sub_plan = GOforward(states,goal, P + [bstate])

            if status == True:
                for i in range(len(sub_plan)):
                    sub_plan[i].plan2str()
                    lis = lis + [(observ, sub_plan[i])]
                    trigger = True

        if len(lis) > 0:
            Policy = Policy + [PlanNode(a, lis)]

    if trigger == True:
        return True, Policy
    else:
        return False, None

def POsolver(instance):
    ''' Your code here '''

    initialStates, goalStates, allActions = instance
    P = [set()]

    state, plan = GOforward(initialStates, goalStates, P)
    #state ,plan1 = GOforward1(initialStates,goalStates, P)
    return plan[0]



        #if plan != None:
            #return PlanNode(a, plan)



    #print("New with depth " + str(plan.plandepth()) + " size " + str(plan.plansize()))

    #return plan

###
###
###
###
###
###
###


