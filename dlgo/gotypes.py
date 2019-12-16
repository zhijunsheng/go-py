import enum
from collections import namedtuple

class Player(enum.Enum):
  black = 1
  white = 2

class Point(namedtuple('Point', 'row col')):
  pass

