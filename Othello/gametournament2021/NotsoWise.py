
#Documentation:
#In this implementation, we modified old Minimax with alpha-beta proning and applied better evalution function
#Evaluation function include (corner_diff, Coin_diff and tested with weighted board)

#All test are done with 5sec constrains.

#Testing results:
#First we tested with corner_diff, it improves the winning rate, but early bad choices may ruin the whole game.
#we added to that coin_diff, if try to get more control at early stages.


#The result is based on best score out of 10: (Same depth 4, time = 5s)
#result against Minimax: 1 0 1 1 1 1 1 1 1 1 out of 10 games it won 9 time (9 out of 10).
#markov is still better


from othello import OthelloState
from agent_interface import AgentInterface
import random

class Agent(AgentInterface):
    """
    An agent who plays the Othello game

    Methods
    -------
    `info` returns the agent's information
    `decide` chooses an action from possible actions
    """
    def __init__(self):
        """
        `depth` is the limit on the depth of Minimax tree
        """
        self.depth = 4
        self.weight = [[4, -3, 2, 2, 2, 2, -3, 4],
                       [-3, -4, -1, -1, -1, -1, -4, -3],
                       [2, -1, 1, 0, 0, 1, -1, 2],
                       [2, -1, 0, 1, 1, 0, -1, 2],
                       [2, -1, 0, 1, 1, 0, -1, 2],
                       [2, -1, 1, 0, 0, 1, -1, 2],
                       [-3, -4, -1, -1, -1, -1, -4, -3],
                       [4, -3, 2, 2, 2, 2, -3, 4]]

    @staticmethod
    def info():
        """
        Return the agent's information

        Returns
        -------
        Dict[str, str]
            `agent name` is the agent's name
            `student name` is the list team members' names
            `student number` is the list of student numbers of the team members
        """
        # -------- Task 1 -------------------------
        # Please complete the following information
        return {"agent name": "NotsoWise",  # COMPLETE HERE
                "student name": ["Amr Alkhashab"],  # COMPLETE HERE
                "student number": ["905833"]}  # COMPLETE HERE

    def decide(self, state: OthelloState, actions: list):
        values = {}
        for action in actions:
            values[action] = self.min_value(state.successor(action), self.depth - 1, float('-inf'), float('inf'))
        max_value = max(values.values())
        candidates = [action for action in actions if (values[action] - max_value > -1)]

        yield random.choice(candidates)

    def eval(self, state):
        return 0.8 * self.corner_diff(state) + 0.15 + 0.1 * self.coin_diff(state) #+ 0.1 * self.board_weight(state)
        #return self.board_weight(state)

    def board_weight(self, state):
        """Measures the difference in the choice_diff in terms of available choices."""
        Player = 0
        Opp = 0
        for i in range(0,8):
            for j in range(0,8):
                if state.getCell(i,j) == state.player:
                   Player=+self.weight[i][j]
                elif state.getCell(i,j) == 3 - state.player:
                    Opp=+self.weight[i][j]
        return  Player - Opp

    def corner_diff(self, state):
        corner = [state.getCell(0, 0), state.getCell(0, 7), state.getCell(7, 0), state.getCell(7, 7)]
        Player = corner.count(state.player)
        Opp = corner.count(3 - state.player)
        if(Player + Opp)!=0:
            return 100*(Player - Opp)/(Player + Opp)
        else:
            return 0

    def coin_diff(self, state):
        Player = state.count(state.player)
        Opp = state.count(3 - state.player)
        return 100*(Player - Opp)/(Player + Opp)


    def max_value(self, state, depth, alpha, beta):
        actions = state.actions()
        if not actions:
            if (not state.previousMoved):
                if (state.count(state.player) > state.count(state.otherPlayer)):
                    return 10000
                if (state.count(state.player) < state.count(state.otherPlayer)):
                    return -10000
                return self.eval(state)
            else:
                if not (depth == 0):
                    return self.min_value(OthelloState(state), depth - 1, alpha, beta)
        if depth == 0:
            return self.eval(state)
            #return state.count(state.player)

        best = float('-inf')
        for action in actions:
            best = max(best, self.max_value(state.successor(action), depth - 1, alpha, beta))
            alpha = max(alpha, best)
            if alpha >= beta:
                break
        return best

    def min_value(self, state, depth, alpha, beta):
        actions = state.actions()
        if not actions:
            if (not state.previousMoved):
                if (state.count(state.player) < state.count(state.otherPlayer)):
                    return 10000
                if (state.count(state.player) > state.count(state.otherPlayer)):
                    return -10000
                return self.eval(state)
            else:
                if not (depth == 0):
                    return self.max_value(OthelloState(state), depth - 1, alpha, beta)
        if depth == 0:
            return self.eval(state)

        best = float('inf')
        for action in actions:
            best = min(best, self.max_value(state.successor(action), depth - 1, alpha, beta))
            beta = min(beta, best)
            if alpha>= beta:
                break

        return best

