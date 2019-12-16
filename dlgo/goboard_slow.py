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
  def __init__(self, board):
    self.board = board

  @classmethod
  def new_game(cls, board_size):
    if isinstance(board_size, int):
      board_size = (board_size, board_size)
    board = Board(*board_size)
    return GameState(board)

