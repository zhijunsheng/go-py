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

  cnt = 0
  while True:
    time.sleep(1.0)

    print(chr(27) + "[2J")
    print_board(game.board)
    print()
    player = gotypes.Player.black if cnt % 2 == 0 else gotypes.Player.white
    cnt += 1
    bot_move = bots[player].select_move(game)
    game = game.apply_move(bot_move)
    

if __name__ == '__main__':
  main()
