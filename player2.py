from collections import defaultdict
import board

class Player2:
  def __init__(self):
    self.placements = []

  def removePlacement(self, board):
    if self.placements:
      mostRecent = self.placements.pop()

      x, y = mostRecent

      board.board[x][y] = '.'

      return True
    
    else:
      print("Player 2. You have no stones to remove.")

      return False

  def checkAndSee(self, coord, board):
    # Parameters:
    # coord (tuple) -> the coordinate of the stone that player 2 has placed during his most recent turn

    # Return:
    # bool -> True if the stone he placed allows player 2 to win, else False

    x, y = coord
    
    self.placements.append(coord)
    
    surroundings = defaultdict(int)

    for i in range(8):
      tmpX, tmpY = x, y

      if i == 0:
        while tmpX >= 0 and tmpY >= 0 and board.board[tmpX][tmpY] == 'x':
          surroundings[i] += 1
          tmpX -= 1
          tmpY -= 1
    
      elif i == 1:
        while tmpX >= 0 and board.board[tmpX][tmpY] == 'x':
          surroundings[i] += 1
          tmpX -= 1
    
      elif i == 2:
        while tmpX >= 0 and tmpY < len(board.board[0]) and board.board[tmpX][tmpY] == 'x':
          surroundings[i] += 1
          tmpX -= 1
          tmpY += 1
    
      elif i == 3:
        while tmpY < len(board.board[0]) and board.board[tmpX][tmpY] == 'x':
          surroundings[i] += 1
          tmpY += 1
    
      elif i == 4:
        while tmpX < len(board.board) and tmpY < len(board.board[0]) and board.board[tmpX][tmpY] == 'x':
          surroundings[i] += 1
          tmpX += 1
          tmpY += 1
    
      elif i == 5:
        while tmpX < len(board.board) and board.board[tmpX][tmpY] == 'x':
          surroundings[i] += 1
          tmpX += 1
    
      elif i == 6:
        while tmpX < len(board.board) and tmpY >= 0 and board.board[tmpX][tmpY] == 'x':
          surroundings[i] += 1
          tmpX += 1
          tmpY -= 1
    
      elif i == 7:
        while tmpY >= 0 and board.board[tmpX][tmpY] == 'x':
          surroundings[i] += 1
          tmpY -= 1

    for i in range(4):
      if surroundings[i] + surroundings[i+4] - 1 >= 5:
        return True
    
    return False
