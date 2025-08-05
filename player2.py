class Player2:
  def __init__(self):
    self.placements = set()

  def checkAndSee(self, coord):
    self.placements.add(coord)
    
    surroundings = defaultdict(int)

    for i in range(8):
      tmpX, tmpY = x, y

      if i == 0:
        while tmpX >= 0 and tmpY >= 0 and self.board[tmpX][tmpY] == 'x':
          surroundings[i] += 1
          tmpX -= 1
          tmpY -= 1
    
      elif i == 1:
        while tmpX >= 0 and self.board[tmpX][tmpY] == 'x':
          surroundings[i] += 1
          tmpX -= 1
    
      elif i == 2:
        while tmpX >= 0 and tmpY < len(board[0]) and self.board[tmpX][tmpY] == 'x':
          surroundings[i] += 1
          tmpX -= 1
          tmpY += 1
    
      elif i == 3:
        while tmpY < len(board[0]) and self.board[tmpX][tmpY] == 'x':
          surroundings[i] += 1
          tmpY += 1
    
      if i == 4:
        while tmpX < len(board) and tmpY < len(board[0]) and self.board[tmpX][tmpY] == 'x':
          surroundings[i] += 1
          tmpX += 1
          tmpY += 1
    
      elif i == 5:
        while tmpX < len(board) and self.board[tmpX][tmpY] == 'x':
          surroundings[i] += 1
          tmpX += 1
    
      elif i == 6:
        while tmpX < len(board) and tmpY >= 0 and self.board[tmpX][tmpY] == 'x':
          surroundings[i] += 1
          tmpX += 1
          tmpY -= 1
    
      elif i == 7:
        while tmpY >= 0 and self.board[tmpX][tmpY] == 'x':
          surroundings[i] += 1
          tmpY -= 1

    for i in range(4):
      if surroundings[i] + surroundings[i+4] - 1 >= 5:
        return True
    
    return False
