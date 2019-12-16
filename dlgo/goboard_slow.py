import copy
from dlgo.gotypes import Player

class Move():
  def __init__(self, point=None, is_pass=False, is_resign=False):
    assert (point is not None) ^ is_pass & is_resign
    self.point = point
    self.is_play = (self.point is not None)
    self.is_pass = is_pass
    self.is_resign = is_resign

  @classmethod
  def play(cls, point):
    return Move(point=point)

  @classmethod
  def pass_turn(cls):
    return Move(is_pass=True)

  @classmethod
  def resign(cls):
    return Move(is_resign=True)

class Board():
  def __init__(self, num_rows, num_cols):
    self.num_rows = num_rows
    self.num_cols = num_cols
    self._grid = {}

  def place_stone(self, player, point):
    self._grid[point] = player

  def get(self, point):
    return self._grid.get(point)

class GameState():
  def __init__(self, board, next_player, previous, move):
    self.board = board
    self.next_player = next_player
    self.previous_state = previous
    self.last_move = move

  def apply_move(self, move):
    if move.is_play:
      next_board = copy.deepcopy(self.board)
      next_board.place_stone(self.next_player, move.point)
    else:
      next_board = self.board
    return GameState(next_board, self.next_player.other, self, move)

  @classmethod
  def new_game(cls, board_size):
    if isinstance(board_size, int):
      board_size = (board_size, board_size)
    board = Board(*board_size)
    return GameState(board, Player.black, None, None)

  def is_over(self):
    if self.last_move is None:
      return False
    if self.last_move.is_resign:
      return True
    second_last_move = self.previous_state.last_move
    if second_last_move is None:
      return False
    return self.last_move.is_pass and second_last_move.is_pass
