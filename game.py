import board
import player1
import player2

class Game:
  def __init__(self, dim):
    self.gameStatus = True
    self.gameBoard = Board(dim)
    self.player1 = Player1()
    self.player2 = Player2()

  def makeMove(self, player, coord):

    if player == 0:
      # black player movement

    else:
      currrentStatus = self.player2.checkAndSee(coord)
      self.gameBoard.placeStone(player, coord)

      if currentStatus:
        # this means that player 2 has won
        self.gameStatus = False
