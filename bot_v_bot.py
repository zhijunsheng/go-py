from dlgo.agent import naive
from dlgo import goboard_slow
from dlgo import gotypes
import time

COLS = 'ABCDEFGHJKLMNOPQRST'
STONE_TO_CHAR = {
  None: '. ',
  gotypes.Player.black: 'x ',
  gotypes.Player.white: 'o ',
}

def testCapture(game):
  game.apply_move(goboard_slow.Move.play(gotypes.Point(5, 10))) 

def print_move(player, move):
  if move.is_pass:
    move_str = 'passes'
  elif move.is_resign:
    move_str = 'resigns'
  else:
    move_str = '%s%d' % (COLS[move.point.col - 1], move.point.row)
  print('%s %s' % (player, move_str))

def print_board(board):
  for row in range(board.num_rows, 0, -1):
    bump = " " if row <= 9 else ""
    line = []
    for col in range(1, board.num_cols + 1):
      stone = board.get(gotypes.Point(row=row, col=col))
      line.append(STONE_TO_CHAR[stone])
    print('%s%d %s' % (bump, row, ''.join(line)))
  print('   ' + ' '.join(COLS[:board.num_cols]))

def main():
  board_size = 19
  bots = {
    gotypes.Player.black: naive.RandomBot(),
    gotypes.Player.white: naive.RandomBot(),
  }
  game = goboard_slow.GameState.new_game(board_size)

#  testCapture(game)

  while not game.is_over():
    time.sleep(2.0)

    print(chr(27) + "[2J")
    print_board(game.board)
    print()
    bot_move = bots[game.next_player].select_move(game)
    print_move(game.next_player, bot_move)
    game = game.apply_move(bot_move)
    

if __name__ == '__main__':
  main()
