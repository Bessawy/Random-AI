
from logic import AND, OR, NOT, ATOM, IMPL, EQVI


# Encoding a scheduling problem into a SAT problem.
#------------------------------------------------------------------------------
#
# In this file, we encode a scheduling problem into a SAT problem. The first
# part of the file provides some helper functions to make the encoding easier.
#
# TASK 1
# ======
# There are two functions that you need to implement:
# `at_most_one`: in this function, you are given a list of formulas, and you
#                need to create a new formula that expresses at least one
#                formula in the list must be true.
# `exactly_one`: in this function, you are given a list of formulas, and you
#                need to create a new formula that expresses exactly one formula
#                in the list must be true.
#
#
#
# In the second part of the file, we encode the scheduling problem into a SAT
# problem:
#
# TASK 2
# ======
# In this task, you will implement the `problem2fma` function to translate a
# scheduling problem into a SAT problem. In other words, you should implement
# the constraints you have learned from the lecture to describe a scheduling
# problem as a SAT problem.
#
# Good luck :)


def all_pairs(lst):
    """
    Helper function, giving all pairs of a list of formulas.

    Parameter
    --------
    lst : list of formulas

    Returns
    -------
    generator of pairs
       Each unique pairing of the formulas in `lst`.
    """

    # return all unique compination ((and A B), (or A C A)) list of toples

    return ((lst[i], lst[j]) for i in range(0, len(lst)) \
            for j in range(i + 1, len(lst)))


def at_least_one(fmas):
    """
    Expresses that at least one formula in a list must be true.

    Parameters
    ----------
    fmas : list of formulas (len > 1)
       Of this list, at least one expression must evaluate to true.

    Returns
    -------
    Formula
    """
    #OR(fmas)
    # At least one true is easy. Disjuction.
    return OR(fmas)


def at_most_one(fmas):
    """
    Expresses that at most one formula in a list must be true.
    Parameters
    ----------
    fmas : list of formulas (len > 1)
       Of this list, at least at most one must be true.

    Returns
    -------
    Formula
    """

    Pairs = all_pairs(fmas)

    size = 0
    for i in range(len(fmas)):
        size = size + len(fmas) - 1 - i

    formula = None
    List = []
    for i in range(size):
        A, B = next(Pairs)
        List.append(AND([A,B]))

    if len(fmas) < 3:
        return NOT(List[0])

    else:
        return NOT(OR(List))
    # Hint: You can use the function 'allpairs' above to get the pairing
    #       of formulas.


def exactly_one(fmas):
    """
    Expresses that exactly one formula in a list must be true.

    Parameters
    ----------
    fmas : list of formulas (expressed as And, Or, Not, or using a Bool Atom).
       Of this list, at least one expression must evaluate to true.

    Returns
    -------
    Formula
    """
    return  AND([at_most_one(fmas), at_least_one(fmas)])


def variable(task, time_slot):
    """
    Creates an atom expressing that `task` should be preformed at `time_slot`

    This is just a wrapper to create a Bool variable (atom) with a string
    representing the particular `task` and `time_slot`

    Parameters
    ----------
    task: str
        Task name
    time_slot: int
        The time slot

    Returns
    -------
    ATOM
        Boolean variable (atom) to be used in formulas. If this variable is
        assigned by the value True, it means the task: `task` should be
        performed at: `time_slot`
    """
    return ATOM("{}@{}".format(task, time_slot))


def problem2fma(tasks, orders, resource_need, time_horizon):


    print("///////////////////////////////////////////////////////////////////////////////////")
    """
    Encodes a scheduling problem to a SAT problem

    Parameters
    ----------
    tasks: List[str]
        A list of strings representing the tasks to be scheduled
    orders: List[(str, str)]
        A list of pairs `(task_1,task_2)`, meaning that `task_1` must
        precede `task_2`
    resource_need: Dict[str, str]
        A dictionary. `resource_need[task] = resource` means that `task`
        needs the `resource`
    time_horizon: int
        An integer which defines the time horizon (the maximum time point)

    Returns
    -------
        The encoded logical formula
    """



    # Tasks must take place exactly once
    C1 = AND([exactly_one([variable(task, t) for t in range(1,time_horizon+1)]) for task in tasks])


    # Tasks with the same resource not simultaneous/ exactly one esources at time

    atm = []
    Clist = []
    for t in range(1, time_horizon+1):
    #taskes need same resources
        List = []
        res = []
        for task in tasks:
            atm = []
            resources = resource_need[task]
            if resources not in res:
                for tas in tasks:
                    if resource_need[tas] == resources:
                        atm.append(variable(tas,t))

                res.append(resources)

            pairs = all_pairs(atm)
            size = 0
            for i in range(len(atm)):
                size = size + len(atm) - 1 - i

            for i in range(size):
                A, B = next(pairs)
                #print(NOT(AND([A, B])), "TESTTTTT")
                List.append(NOT(AND([A, B])))
                #print(List[-1], "Test2")


        if List != []:
            Clist.append(AND(List))


    #print("////////////////////////////////////////////////////////////////////////////////CCCCCCCCCCCCCCCCCCC")
    #print(Clist[-1])
    #print("///////////////////////////////////////////////////////////////////////////////")

    C2 = AND(Clist)




    # Ordering of operations of a job must be obeyed



    order = []
    i = 0
    j=0
    for task1, task2 in orders:
        if task1 not in order and i == 0:
            order.append([task1,task2])
        elif task1 == order[j][-1]:
            order[j].append(task2)
        else:
            j =j + 1
            order.append([task1, task2])

        i = i + 1

    #print("order",order[0])

    atm2 = []
    cc = []
    for t in range(1, time_horizon+1):
        for i in range(len(order)):
            for j in range(len(order[i])):
                atm2 = []
                for f in range(j ,len(order[i])):
                    for K in range(1, t):
                        atm2.append(NOT(variable(order[f][j], K)))

                if atm2 != []:
                    if len(atm2) > 1:
                        cc.append(IMPL(variable(order[i][j], t), AND(atm2)))
                    else:
                        cc.append(IMPL(variable(order[i][j], t), atm2[0]))

                    #print(IMPL(variable(order[i][j], t), AND(atm2)))
                #print("///////////////////////////////////////////////////////////")

                #print("-------------------------------------------------------------")

    Big= []
    for t in range(1, time_horizon+1):
        for i in range(len(order)):
            for j in range(len(order[i])):
                atom = []
                for k in range(j, len(order[i])):
                    for M in range(1, t+1):
                        if order[i][j] == order[i][k] and t == M:
                            X = None
                        else:
                            atom.append(NOT(variable(order[i][k], M)))
                if atom != []:
                    if len(atom) > 1:
                        Big.append(IMPL(variable(order[i][j], t), AND(atom)))
                    else:
                        Big.append(IMPL(variable(order[i][j], t), atom[0]))


    #for i in range(1,time_horizon+1):




    C3 = AND(Big)




    #C3 = ### IMPLEMENT THIS ## IMPLEMENT THIS ## IMPLEMENT THIS ## IMPLEMENT THIS ###


    return AND([C1,C2,C3])


