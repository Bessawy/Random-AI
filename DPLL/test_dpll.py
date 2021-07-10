import unittest
from dpll import dpll
from logic import ATOM, AND, OR, NOT, IMPL, EQVI
from z3_wrapper import solve
from random import seed, randint


seed(0)


class MyTestCase(unittest.TestCase):
    def check(self, formula):
        model = dict()
        my_result = dpll(model, formula.clauses(), formula.vars())
        z3_result, _, _ = solve(formula.clauses())
        sat_to_string = {True: 'Satisfiable', False: 'Unsatisfiable'}
        self.assertEqual(z3_result, my_result, "Expected value: {}, Actual value: {}".format(sat_to_string[z3_result],
                                                                                             sat_to_string[my_result]))
        if my_result:
            self.assertTrue(formula.is_satisfiable(model), "Valuation is not correct")
        return my_result

    def test_simple_positive_literal(self):
        formula = ATOM("x")
        self.check(formula)

    def test_simple_negative_literal(self):
        formula = NOT(ATOM("x"))
        self.check(formula)

    def test_simple_unsat(self):
        formula = AND([ATOM("x"), NOT(ATOM("x"))])
        result = self.check(formula)
        self.assertFalse(result, "`x and not(x)` is UNSAT")

    def test_simple_two_variables_1(self):
        x = ATOM('x')
        y = ATOM('y')
        formula = AND([OR([x, y]), OR([NOT(x), NOT(y)])])
        self.check(formula)

    def test_simple_two_variables_2(self):
        x = ATOM('x')
        y = ATOM('y')
        formula = AND([IMPL(x, y), IMPL(y, x)])
        self.check(formula)

    def test_simple_two_variables_3(self):
        x = ATOM('x')
        y = ATOM('y')
        formula = AND([EQVI(x, y), NOT(x)])
        self.check(formula)

    def test_3SAT_1(self):
        x = ATOM('x')
        y = ATOM('y')
        z = ATOM('z')
        clauses = list()
        clauses.append(OR([x, NOT(y), z]))
        clauses.append(OR([NOT(x), y, NOT(z)]))
        clauses.append(OR([NOT(x), NOT(y)]))
        clauses.append(OR([x, y, z]))
        formula = AND(clauses)
        self.check(formula)


if __name__ == '__main__':
    unittest.main()
