#!/usr/bin/python3

from pacman import *


GRID1 = PacManGrid(["......",
                    ".XX.X.",
                    "......"])
ISTATE1 = PacManState(0,0,"N",GRID1)
print(ISTATE1.successors())