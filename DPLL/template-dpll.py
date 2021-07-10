# DPLL: The Davis-Putnam-Logemann-Loveland (DPLL) algorithm
#
# The most basic way of testing satisfiability is equivalent to the
# truth-table method: exhaustively generate all 2^n valuations with
# a binary tree of depth n, with each leave representing a valuation and
# each inner node representing case analysis on the two possible values
# of a propositional variable.
#
# The Davis-Putnam procedure improves on this by performing Unit Propagation
# after each case analysis: some variable must have a certain value, because
# otherwise one of the clauses would be false, and instead of doing a case
# analysis on that variable, we will assign the forced value to the variable.
#
# What Unit Propagation does is to identify clauses l1 V l2 V ... V Ln
# that does not contain any True literals under the current (partial) valuation,
# and that contains n-1 False literals. The remaining literal (which does not
# have a value) must be made True, because otherwise the clause and the whole
# clause set would be False. If the literal is positive, assign the variable in
# it True, and otherwise the literal is negative and assign the variable False.
#
# This, relatively simple, improvement makes it possible to solve orders of
# magnitudes harder satisfiability problems than what is possible with the truth-table
# method. Additional improvements in implementation technology (best possible
# data structures, minimization of cache misses etc.) as well as clever ways
# of choosing the variables for case analysis, and many other improvements,
# have lifted the scalability of SAT solving still dramatically further in
# the past 25 years.


def dpll(valuation, clauses, variables):
    """
    The Davis-Putnam-Logemann-Loveland (DPLL) algorithm

    Determines if a Conjunctive Normal Form (CNF) formula is satisfiable or not;
    if the formula is satisfiable, it specifies the truth values of the
    variables.

    The CNF formula is given as a list of clauses; each clause is a list of
    literals and a literal is a propositional variable or its negation. Here,
    We represent a literal with a pair of (str, bool), where the first element
    represent the variable, and its second element represent the polarity of the
    literal.

    Parameters
    ----------
    valuation: Dict[str, bool]
        Current partial valuation of the propositional variables. It maps the
        name of variables to their assigned truth-values.
    clauses: List[List[(str, bool)]]
        The CNF formula; Literals are described by a pair of (str, bool), which
        denotes the variable and its polarity, respectively.
    variables: List[str]
        List of variables.

    Returns
    -------
    bool
        If the formula is satisfiable, it returns `True`; otherwise, it returns
        `False`. If the return value is `True`, the `valuation` dictionary has
        been updated so that it specifies all variables' truth-values.
    """

    #                                   TASK
    # -------------------------------------------------------------------------
    # Implement the DPLL algorithm.
    #
    # The first step to develop the DPLL algorithm is to implement the unit
    # propagation procedure. This procedure should find all unsatisfied clauses
    # with only one unassigned literal (these clauses are called unit clauses);
    # thus, the remaining literal has just one possible value to satisfy the
    # clause. For example, let assume the input is:
    #
    # valuation = {'a': True}
    # clauses = [[('a', False), ('b', True) ],
    #            [('b', False), ('c', False)],
    #            [('d': True),  ('e': False)]]
    # variables = ['a', 'b', 'c', 'd', 'e']
    #
    # It means the given formula is: (¬a ∨ b) ∧ (¬b ∨ ¬c) ∧ (d ∨ ¬e)
    # and, until now, we assume the value of `a` is `True`.
    #
    # The only unsatisfied clause that has just one unassigned literal is
    # `[('a', False), ('b', True)]`, so, to satisfy this clause, we need to
    # assign the value of `True` to `b`.
    # It is possible that applying unit propagation makes some other clauses
    # become new unit clauses. Thus, in the unit propagation procedure, we
    # should continue searching until there is no other unit clause in the
    # clause set.
    # In our example, after updating `valuation` to `{'a': True, 'b': True}`,
    # the clause `[('b', False), ('c', False)]` becomes a new unit clause; so,
    # we can update `valuation` to `{'a': True, 'b': True, 'c': False}`. After
    # this update, the clause set will have no other unit clause anymore.
    #
    # After unit propagation, we need to choose an unassigned variable and test
    # whether assigning `True` to it makes the formula satisfiable or assigning
    # `False` (These tests can be done by updating the `valuation` dictionary
    # and calling `dpll` function recursively). If none of those values makes
    # the formula satisfiable, then it is unsatisfiable, and this function
    # should return `False`.
    # If there is no unassigned variable, then the value of all variables are
    # specified, and we should return `True`.
    #
    # =====
    # Tips
    # =====
    # 1. By performing a unit propagation, you may realize that the current
    #    valuation makes the formula unsatisfiable; in this case, you should
    #    declare that the formula is unsatisfiable.
    # 2. Objects in python are passed by their references when used as
    #    arguments in function calls; therefore, if you modify the `valuation`
    #    dictionary and later become aware that the formula is unsatisfiable,
    #    you should undo all of your modifications. The other approach is to
    #    back up a copy of `valuation` before calling the `dpll` function, and
    #    if it returns `False`, you can restore its copied version.
    # 3. You can use the most simple version of the unit propagation procedure,
    #    which its pseudocode is provided in the course materials.
    #
    # Good luck :)
    # -------------------------------------------------------------------------
