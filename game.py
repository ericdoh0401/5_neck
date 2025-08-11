import board
import player1
import player2
from collections import defaultdict

class Game:
  def __init__(self, dim):
    self.gameStatus = True
    self.gameBoard = board.Board(dim)
    self.player1 = player1.Player1()
    self.player2 = player2.Player2()

  def makeMove(self, player, coord):
    # Paramters:
    # player (int) -> the player who is to place the stone
    # coord (tuple) -> the coordinate of the stone the player wishes to place

    # Return:
    # bool -> True if the stone the player places is a valid placement, thus moving onto the next player. False otherwise
    x, y = coord

    if self.gameBoard.board[x][y] != '.':
      return False

    if player == 0:
      valid = self.player1.isValidPlacement(coord, self.gameBoard)
      if not valid:
        print("This is not a valid placement for your stone. Either it creates a connect-6 or greater or you have created a 삼삼.")
        return False

      self.gameBoard.placeStone(player, coord)
      currentStatus = self.player1.makeFive()

      if currentStatus:
        self.gameStatus = False

      return True
      # black player movement

    else:
      self.gameBoard.placeStone(player, coord)
      currentStatus = self.player2.checkAndSee(coord, self.gameBoard)

      if currentStatus:
        # this means that player 2 has won and the game has ended
        self.gameStatus = False

      return True
