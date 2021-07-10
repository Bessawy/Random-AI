import unittest
import random
from dpll import dpll
from logic import ATOM, AND, OR, NOT, IMPL, EQVI
from z3_wrapper import solve


random.seed(0)


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


    def test_random_3SAT(self):
        print("Tet")
        variables = [ATOM(i) for i in "abcdefghijklmno"]
        number_of_formulas = 40
        number_of_clauses = 75
        for i in range(number_of_formulas):

            clauses = list()
            while len(clauses) < number_of_clauses:
                clause = list()
                for _ in range(3):
                    literal = random.choice(variables)
                    if random.random() < 0.5:
                        literal = NOT(literal)
                    clause.append(literal)
                clauses.append(OR(clause))
            formula = AND(clauses)
            if i == 4:
                print("error///////////////////////////////////////////////")
            self.check(formula)
            print("DONE=====================================", i)





if __name__ == '__main__':
    unittest.main()
