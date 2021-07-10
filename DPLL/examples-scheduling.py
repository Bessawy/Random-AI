
#!/usr/bin/python3
from time import time
from scheduling import problem2fma, variable
import z3_wrapper

DO_YOU_WANT_TO_COMPARE_YOUR_DPLL_WITH_Z3 = False  # <-------- IF YOU WANT TO COMPARE YOUR DPLL WITH Z3, ENABLE THIS


def show_the_scheduling(model, tasks, time_horizon, is_z3_used):
    """
    Shows the solution for the scheduling problem

    Parameters
    ----------
    model: Dict[str, bool] or Dict[z3.Bool, bool]
        A dictionary that maps variables to their truth-values.
        If we used our DPLL, then its type is: Dict[str, bool].
        Otherwise, if we used Z3, then its type is:
        Dict[z3.Bool, bool]
    tasks: List[str]
        A list of strings representing the tasks to be scheduled
    time_horizon: int
        An integer which defines the time horizon (the maximum time point)
    is_z3_used: bool
        Specifies if the `model` is produced by Z3 or by our DPLL
    """
    max_task_name_length = max(len(task) for task in tasks)
    result = {}
    for t in range(1, time_horizon + 1):
        print("Time horizon: {}".format(t), end=' ')
        for task in tasks:
            variable_name = variable(task, t).name
            if model[variable_name if not is_z3_used else z3_wrapper.Bool(variable_name)]:
                result[task] = t
                print(task, end=' ')
                for a in range(len(task), max_task_name_length):
                    print("", end=' ')
        print("")
    return result


def solve_problem(tasks, orders, resource_need, max_time):
    """
    Solves a scheduling problem by reduction to SAT

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
    max_time: int
        An integer which defines the time horizon (the maximum time point)
    """
    print("Horizon", end=' ')
    print(str(max_time))

    formula = problem2fma(tasks, orders, resource_need, max_time)
    clauses = formula.clauses()
    result = {True: "Satisfiable", False: "Unsatisfiable"}

    if DO_YOU_WANT_TO_COMPARE_YOUR_DPLL_WITH_Z3:
        from dpll import dpll

        starting_time = time()
        variables = sorted(formula.vars())
        model = dict()
        is_satisfiable = dpll(model, formula.clauses(), variables)
        my_duration = time() - starting_time
        print("DPLL result:", end=' ')
        print(result[is_satisfiable])
        print("DPLL time: {} seconds".format(my_duration))
        if is_satisfiable:
            show_the_scheduling(model, tasks, max_time, False)
        print("========================================")

    z3_result, model, z3_duration = z3_wrapper.solve(clauses)
    print("Z3 result:", end=' ')
    print(result[z3_result])
    print("Z3 time : {}(s)".format(z3_duration))
    if z3_result:
        return show_the_scheduling(model, tasks, max_time, True)
    else:
        return None


def main():
    # Task 1: The scheduling problem from the slides
    print("Task 1: Scheduling problem form the slides")

    tasks1 = ["1R", "1B", "1G", "2R", "2B", "2G", "3R", "3B", "3G"]
    print(tasks1)
    orders1 = [("1R", "1B"), ("1B", "1G"), ("2B", "2G"), ("2G", "2R"), ("3B", "3R"), ("3R", "3G")]
    resourceNeed1 = {"1R": "Red", "2R": "Red", "3R": "Red", "1G": "Green", "2G": "Green", "3G": "Green", "1B": "Blue",
                     "2B": "Blue", "3B": "Blue"}
    solve_problem(tasks1, orders1, resourceNeed1, 5)
    print("##########################################")

    # Task 2
    # you can easily produce your own test cases in the same way


if __name__ == "__main__":
    main()
