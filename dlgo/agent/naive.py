import random
from dlgo.agent.base import Agent
from dlgo import gotypes

class RandomBot(Agent):
  def select_move(self):
    candidates = []
    for row in range(1, 19):
      for col in range(1, 19):
        candidates.append(gotypes.Point(row, col))
    return random.choice(candidates)
