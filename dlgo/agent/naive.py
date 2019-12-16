import random
from dlgo.agent.base import Agent
from dlgo import gotypes
from dlgo.goboard_slow import Move

class RandomBot(Agent):
  def select_move(self, game_state):
    candidates = []
    for row in range(1, game_state.board.num_rows + 1):
      for col in range(1, game_state.board.num_cols + 1):
        candidates.append(gotypes.Point(row, col))
    return Move.play(random.choice(candidates))
