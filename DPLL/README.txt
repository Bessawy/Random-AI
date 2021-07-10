Programming exercise: DPLL and Scheduling
--------------------------------------------------------------------------------

In this exercise, you will implement the DPLL algorithm and encode the
constraints of a scheduling problem.

Instructions
============
1. In this exercise, you need the Z3 SMT solver; to install it, you can use the
   following command:

   `pip install z3-solver`

   See https://github.com/Z3Prover/z3 for more information.
2. Copy the file `template-dpll.py` to `dpll.py`.
3. Read its documentation and complete the code.
4. Test your implementation and verify its correctness. We have provided some
   unit tests in `test_dpll.py` to make your life a little easier :)
5. Copy the file `template-scheduling.py` to `scheduling.py`.
6. Read and understand the `logic.py` and `scheduling.py` files.
7. Complete the required sections in `scheduling.py`.
8. Test your implementation and verify its correctness. There are some examples
   to help you for testing your encoding.
9. Well done! Submit your code.


Example
=======
As an example, we have provided the encoding of Sudoku problems for SAT solvers.
You can see the encoding in the `sudoku.py` file.


Testing
=======
1. `python test_dpll.py`: performs some basic unit tests on your DPLL
   implementation.
2. `python example-scheduling.py`: Using your encoding, it tries to define some
   basic scheduling problems for SAT solvers. Then, it feeds the encoded problem
   to the SAT solver and shows its result.
3. `python example-sudoku.py`: Using your DPLL implementation, it tries to solve
   the encoded Sudoku problems. Besides testing your DPLL implementation, you
   can compare your run-time against the Z3 solver with this script. Moreover,
   you can solve your own Sudoku problems with this script ;)


GL HF :)
