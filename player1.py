from collections import defaultdict
import board

class Player1:
  def __init__(self):
    self.placements = set()
    self.surroundings = defaultdict(list)
    self.isValid = False

  def isSixGreater(self, con1, con2):
    if con1 + con2 - 1 >= 6:
      return True

    return False

  def makeFive(self):
    if self.isValid:
      for i in range(4):
        len1, len2 = self.surroundings[i], self.surroundings[i+4]

        con1, con2 = len1[0], len2[1]

        if con1 + con2 - 1 == 5:
          return True

    return False

  def isValidPlacement(self, coord, board):
    self.blackSurroundings(coord, board)
    
    x, y = coord
    print(self.surroundings)
    # defaultdict(<class 'list'>, {0: [1, 0], 1: [2, 0], 2: [1, 0], 3: [2, 0], 4: [1, 0], 5: [2, 0], 6: [1, 0], 7: [2, 0]})
    # (5,5) -> (4,6) -> (4,4) -> (3,5) -> (4,5)
    board.board[x][y] = '.'

    numberOfThrees, longestLengths = 0, defaultdict(int)

    for i in range(4):
      len1, len2 = self.surroundings[i], self.surroundings[i+4]

      con1, sep1, con2, sep2 = len1[0], len1[1], len2[0], len2[1]

      if self.isSixGreater(con1, con2):
        return False

      longestLengths[i] = max(con1 + sep2, con2 + sep1)

    for i in range(3):
      for j in range(i+1, 4):
        if longestLengths[i] == 3 and longestLengths[j] == 3:
          return False

    board.board[x][y] = 'o'
    self.isValid = True
    return True

  def blackSurroundings(self, coord, board):
    x, y = coord
    board.board[x][y] = 'o'

    self.surroundings = defaultdict(list)
    self.isValid = False

    for i in range(8):
      self.surroundings[i] = [0, 0]
      tmpX, tmpY = coord
      stack, cnt = [], 0

      if i == 0:
        while tmpX >= 0 and tmpY >= 0 and board.board[tmpX][tmpY] == 'o':
          self.surroundings[i][0] += 1
          tmpX -= 1
          tmpY -= 1

        while cnt < 2 and tmpX >= 0 and tmpY >= 0 and (board.board[tmpX][tmpY] == 'o' or board.board[tmpX][tmpY] == '.'):
          if board.board[tmpX][tmpY] == 'o':
            self.surroundings[i][1] += 1

          else:
            cnt += 1

          tmpX -= 1
          tmpY -= 1
    
      elif i == 1:
        while tmpX >= 0 and board.board[tmpX][tmpY] == 'o':
          self.surroundings[i][0] += 1
          tmpX -= 1
      
        while cnt < 2 and tmpX >= 0 and (board.board[tmpX][tmpY] == 'o' or board.board[tmpX][tmpY] == '.'):
          if board.board[tmpX][tmpY] == 'o':
            self.surroundings[i][1] += 1

          else:
            cnt += 1

          tmpX -= 1
      
      elif i == 2:
        while tmpX >= 0 and tmpY < len(board.board[0]) and board.board[tmpX][tmpY] == 'o':
          self.surroundings[i][0] += 1
          tmpX -= 1
          tmpY += 1
      
        while cnt < 2 and tmpX >= 0 and tmpY < len(board.board[0]) and (board.board[tmpX][tmpY] == 'o' or board.board[tmpX][tmpY] == '.'):
          if board.board[tmpX][tmpY] == 'o':
            self.surroundings[i][1] += 1

          else:
            cnt += 1

          tmpX -= 1
          tmpY += 1

      elif i == 3:
        while tmpY < len(board.board[0]) and board.board[tmpX][tmpY] == 'o':
          self.surroundings[i][0] += 1
          tmpY += 1

        while cnt < 2 and tmpY < len(board.board[0]) and (board.board[tmpX][tmpY] == 'o' or board.board[tmpX][tmpY] == '.'):
          if board.board[tmpX][tmpY] == 'o':
            self.surroundings[i][1] += 1

          else:
            cnt += 1

          tmpY += 1

      elif i == 4:
        while tmpX < len(board.board) and tmpY < len(board.board[0]) and board.board[tmpX][tmpY] == 'o':
          self.surroundings[i][0] += 1
          tmpX += 1
          tmpY += 1

        while cnt < 2 and tmpX < len(board.board) and tmpY < len(board.board[0]) and (board.board[tmpX][tmpY] == 'o' or board.board[tmpX][tmpY] == '.'):
          if board.board[tmpX][tmpY] == 'o':
            self.surroundings[i][1] += 1

          else:
            cnt += 1

          tmpX += 1
          tmpY += 1
        
      elif i == 5:
        while tmpX < len(board.board) and board.board[tmpX][tmpY] == 'o':
          self.surroundings[i][0] += 1
          tmpX += 1

        while cnt < 2 and tmpX < len(board.board) and (board.board[tmpX][tmpY] == 'o' or board.board[tmpX][tmpY] == '.'):
          if board.board[tmpX][tmpY] == 'o':
            self.surroundings[i][1] += 1

          else:
            cnt += 1
            
          tmpX += 1

      elif i == 6:
        while tmpX < len(board.board) and tmpY >= 0 and board.board[tmpX][tmpY] == 'o':
          self.surroundings[i][0] += 1
          tmpX += 1
          tmpY -= 1

        while cnt < 2 and tmpX < len(board.board) and tmpY >= 0 and (board.board[tmpX][tmpY] == 'o' or board.board[tmpX][tmpY] == '.'):
          if board.board[tmpX][tmpY] == 'o':
            self.surroundings[i][1] += 1

          else:
            cnt += 1
            
          tmpX += 1
          tmpY -= 1
          
      elif i == 7:
        
        while tmpY >= 0 and board.board[tmpX][tmpY] == 'o':
          self.surroundings[i][0] += 1
          tmpY -= 1
          
        while cnt < 2 and tmpY >= 0 and (board.board[tmpX][tmpY] == 'o' or board.board[tmpX][tmpY] == '.'):
          if board.board[tmpX][tmpY] == 'o':
            self.surroundings[i][1] += 1

          else:
            cnt += 1
            
          tmpY -= 1
      


        
        
