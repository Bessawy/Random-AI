# DPLL: The Davis-Putnam-Logemann-Loveland (DPLL) algorith


# What Unit Propagation does is to identify clauses l1 V l2 V ... V Ln
# that does not contain any True literals under the current (partial) valuation,
# and that contains n-1 False literals. The remaining literal (which does not
# have a value) must be made True, because otherwise the clause and the whole
# clause set would be False. If the literal is positive, assign the variable in
# it True, and otherwise the literal is negative and assign the variable False.



def allTrue(clauses, valuation):  # at least one member of model in each clause
    for clause in clauses:
        positive  = False
        for atm,bool in clause:
            if atm in valuation:
                if (valuation[atm] == 1 and bool == True) or (valuation[atm] == 0 and bool == False):
                    positive = True
        if positive == False:
            return False

    return True

def someFalse(clauses, valuation):  # some clause cannot be satisfied
    for clause in clauses:
        Negative = 0
        for atm, bool in clause:
            if atm not in valuation:
                break
            elif (valuation[atm] == 0 and bool == True) or (valuation[atm] == 1 and bool == False):
                Negative = Negative + 1

        if Negative == len(clause):
            return True
    return False


def unitClause(clauses, valuation):# finds 1 literal not in model appearing by itself in a clause
    valuation_backup = valuation.copy()
    for i in range(len(clauses)):
        for clause in clauses:
            NumberOfNeG = 0
            unsigned = 0
            unbool = 0
            var = 0
            for atm,bool in clause:
                if atm in valuation_backup:
                    if (valuation_backup[atm] == 1 and bool == 0) or (valuation_backup[atm] == 0 and bool == 1):
                        NumberOfNeG = NumberOfNeG + 1
                else:
                    unbool = bool
                    var = atm
                    unsigned = unsigned + 1
            if unsigned == 1 :
                if NumberOfNeG == len(clause) - 1:
                    valuation_backup[var] = unbool
                    #valuation.update(valuation_backup)

            if someFalse(clauses, valuation):
                return False, valuation
    return True, valuation_backup





def dpll(valuation, clauses, variable):

    result, val_back = unitClause(clauses,valuation)

    if result == False:
        return False

    if allTrue(clauses, val_back):
        #val_back = valuation.copy()

        for var in variable:
            if var not in val_back:
                val_back[var] = 1

        valuation.update(val_back)
        return True


    x = None
    for var in variable:
        if var not in val_back:
            x = var
            break

    valuation_backup = val_back.copy()
    #valuation.update({x: 1})
    val_back[x] = 1


    result = dpll(val_back, clauses, variable)
    if result != False:
        valuation.update(val_back)
        return True

    valuation_backup[x] = 0
    result = dpll(valuation_backup, clauses, variable)
    if result != False:
        valuation.update(valuation_backup)
        return True
    else:
        return False






