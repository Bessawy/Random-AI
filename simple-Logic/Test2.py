#!/usr/bin/python3

import itertools
from itertools import compress, product
# Representation of propositional formulas in Python.
#
# The basic connectives are NOT, AND and OR.
# IMPL and EQVI are reduced to these through the obvious equivalences.
# Separate classes represent each connective, atomic formulas, and
# the constants TRUE and FALSE.
#
# The methods supported are:
#   vars(self)          Set of all variables occurring in a formula
#   truthValue(self,v)  Compute truth value under valuation 'v'
#
# Valuations are represented by sets/lists consisting of the names
# of those atomic formulas that are True. For example, the empty
# set/list corresponds to the valuation in which all atomic formulas
# are False. To test if the formula ATOM("a") is true in a valuation
# V, one tests if "a" is an element of the set/list V.

# Superclass to handle parts of AND and OR

class BinaryFormula:
  def __init__(self,subformula1,subformula2):
    self.subformula1 = subformula1
    self.subformula2 = subformula2
  def vars(self):
    return self.subformula1.vars().union(self.subformula2.vars())

# Both AND and OR will inherit __init__ and vars from BinaryFormula

# AND - conjunction

class AND(BinaryFormula):
  def __repr__(self):
    return "(" + str(self.subformula1) + " AND " + str(self.subformula2) + ")"
  def truthValue(self,v):
    return self.subformula1.truthValue(v) and self.subformula2.truthValue(v)
### IMPLEMENT THIS (~ 1 line)

# OR - disjunction

class OR(BinaryFormula):
  def __repr__(self):
    return "(" + str(self.subformula1) + " OR " + str(self.subformula2) + ")"
  def truthValue(self,v):
    return self.subformula1.truthValue(v) or self.subformula2.truthValue(v)
### IMPLEMENT THIS (~ 1 line)

# NOT - negation

class NOT:
  def __init__(self,subformula):
    self.subformula = subformula
  def __repr__(self):
    return "(not " + str(self.subformula) + ")"
  def vars(self):
    return self.subformula.vars()
  def truthValue(self,v):
    return not self.subformula.truthValue(v)
### IMPLEMENT THIS (~ 1 line)

# ATOM - atomic formulas

class ATOM:
  def __init__(self,name):
    self.name = name
  def __repr__(self):
    return self.name
  def vars(self):
    return {self.name}
  def truthValue(self,v):
    return self.name in str(v)
### IMPLEMENT THIS (~ 1 line)

# FALSE - the constant that represents the truth-value False

class FALSE:
  def __repr__(self):
    return "FALSE"
  def vars(self):
    return set()
  def truthValue(self,v):
    return self in v
### IMPLEMENT THIS (~ 1 line)

# TRUE - the constant that represents the truth-value True

class TRUE:
  def __repr__(self):
    return "TRUE"
  def vars(self):
    return set()
  def truthValue(self,v):
    print(self in v)
    return self in v
### IMPLEMENT THIS (~ 1 line)


# Implication and equivalence reduced to the primitive connectives

# A -> B is reduced to -A V B

def IMPL(f1,f2):
  return OR(NOT(f1),f2)

# A <-> B is reduced to (A -> B) & (B -> A)

def EQVI(f1,f2):
  return AND(IMPL(f1,f2),IMPL(f2,f1))

def chainAND(l):
  if l == []:
    return TRUE()
  elif len(l) == 1:
    return l[0]
  else:
    return AND(l[0],chainAND(l[1:]))


A = ATOM("A")
B = ATOM("B")
C = ATOM("C")
D = ATOM("D")
E = ATOM("E")
F = ATOM("F")
G = ATOM("G")
H = ATOM("H")
I = ATOM("I")
J = ATOM("J")
K = ATOM("K")
L = ATOM("L")
M = ATOM("M")
N = ATOM("N")
O = ATOM("O")
P = ATOM("P")
Q = ATOM("Q")
R = ATOM("R")
S = ATOM("S")
T = ATOM("T")
U = ATOM("U")
V = ATOM("V")
W = ATOM("W")
X = ATOM("X")
Y = ATOM("Y")
Z = ATOM("Z")


def combs(a):
  if len(a) == 0:
    return [[]]
  cs = []
  for c in combs(a[1:]):
    cs += [c, c + [a[0]]]
  return cs

# Simple tests to see if 'satisfiable' works correctly:
def satisfiable(f):
  Models = []
  satisfy = False
  vars = f.vars()
  possModel = combs(list(vars))
  for i in range(len(possModel)):
    Val = f.truthValue(set(possModel[i]))
    if Val == True:
      satisfy = True
      Models.append(possModel[i])
  if satisfy == False:
    return False
  else:
    return Models


def logicalConsequence(f1,f2):
  return not(satisfiable(AND(f1,NOT(f2))))



f1 = AND(A,B)
f2 = OR(A, AND(B,C))

f3 = A
#new - EQVI(B, OR(NOT(A),C))
#f4 - IMPL(C,NOT(A))
#f5 = IMPL(NOT(A), NOT(C))

print("new2w")
print(logicalConsequence(IMPL(C,NOT(A)),EQVI(B, OR(NOT(A),C))))
