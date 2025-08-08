# understand that the player who goes first is not allowed to make 3 x 3.

# this class will solely be used for the purpose of displaying the board
# and any possible animations using pygame

class Board:
  def __init__(self, dim):
    self.board = [['.' for _ in range(dim)] for _ in range(dim)]

  def displayBoard(self):
    for row in self.board:
      print(row)

  def placeStone(self, player, coord) -> list:
    x, y = coord

    if player == 0:
      self.board[x][y] = 'o'
      
    else:
      self.board[x][y] = 'x'
