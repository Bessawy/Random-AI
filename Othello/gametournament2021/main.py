from game import Game
from random_agent import RandomAgent
from markov_agent import MarkovAgent
from minimax_agent import MinimaxAgent
from agent import Agent


def main():
    # game = Game(RandomAgent(), MarkovAgent())
    # game = Game(RandomAgent(), MinimaxAgent(4))
    # game = Game(MarkovAgent(), MinimaxAgent(4))
    #game = Game(Agent(), MarkovAgent())
    game = Game(MinimaxAgent(4), Agent())
    game.play(output=True, timeout_per_turn=5.0)


if __name__ == "__main__":
    main()
