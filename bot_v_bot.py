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

def makeMove(game, r, c):
  return game.apply_move(goboard_slow.Move.play(gotypes.Point(r, c))) 
def testCapture(game):
  print(chr(27) + "[2J")
  game = makeMove(game, 5, 10)
  game = makeMove(game, 6, 10) 
  game = makeMove(game, 5, 11) 
  game = makeMove(game, 6, 11) 
  game = makeMove(game, 6, 9) 
  game = makeMove(game, 1, 1)
  game = makeMove(game, 6, 12) 
  game = makeMove(game, 2, 1)
  game = makeMove(game, 7, 10) 
  game = makeMove(game, 3, 1)
  print_board(game.board)
  time.sleep(5.0)
  game = makeMove(game, 7, 11) 
  print(chr(27) + "[2J")
  print_board(game.board)
  game = makeMove(game, 4, 1)
  return game

def main():
  board_size = 19
  bots = {
    gotypes.Player.black: naive.RandomBot(),
    gotypes.Player.white: naive.RandomBot(),
  }
  game = goboard_slow.GameState.new_game(board_size)

  game = testCapture(game)

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
