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
        con1, con2 = len1[0][1], len2[0][1]

        if con1 + con2 - 1 == 5:
          return True

    return False

  def isValidPlacement(self, coord):
    surr = self.blackSurroundings(coord)

    numberOfThrees, longestLengths = 0, defaultdict(int)

    for i in range(4):
      len1, len2 = surr[i], surr[i+4]

      con1, sep1, con2, sep2 = len1[0][1], len1[1][1], len2[0][1], len2[1][1]

      if self.isSixGreater(con1, con2):
        return False

      longestLengths[i] = max(con1 + sep2, con2 + sep1)

    for i in range(3):
      for j in range(i+1, 4):
        if longestLengths[i] == 3 and longestLengths[j] == 3:
          return False

    self.isValid = True
    return True

  def blackSurroundings(self, coord):

    self.surroundings = defaultdict(list)
    self.isValid = False

    for i in range(8):
      surroundings[i] = [['con', 0], ['sep', 0]]
      stack, tmpX, tmpY, cnt = [], 0, 0, 0

      if i == 0:
        while tmpX >= 0 and tmpY >= 0 and self.board[tmpX][tmpY] == 'o':
          suroundings[i][0][1] += 1
          tmpX -= 1
          tmpY -= 1

        while cnt < 2 and tmpX >= 0 and tmpY >= 0 and (self.board[tmpX][tmpY] == 'o' or self.board[tmpX][tmpY] == '.'):
          if self.board[tmpX][tmpY] == 'o':
            surroundings[i][1][1] += 1

          else:
            cnt += 1

          tmpX -= 1
          tmpY -= 1
    
      elif i == 1:
        while tmpX >= 0 and self.board[tmpX][tmpY] == 'o':
          suroundings[i][0][1] += 1
          tmpX -= 1
      
        while cnt < 2 and tmpX >= 0 and (self.board[tmpX][tmpY] == 'o' or self.board[tmpX][tmpY] == '.'):
          if self.board[tmpX][tmpY] == 'o':
            surroundings[i][1][1] += 1

          else:
            cnt += 1

          tmpX -= 1
      
      elif i == 2:
        while tmpX >= 0 and tmpY < len(board[0]) and self.board[tmpX][tmpY] == 'o':
          suroundings[i][0][1] += 1
          tmpX -= 1
          tmpY += 1
      
        while cnt < 2 and tmpX >= 0 and tmpY < len(board[0]) and (self.board[tmpX][tmpY] == 'o' or self.board[tmpX][tmpY] == '.'):
          if self.board[tmpX][tmpY] == 'o':
            surroundings[i][1][1] += 1

          else:
            cnt += 1

          tmpX -= 1
          tmpY += 1

      elif i == 3:
        while tmpY < len(board[0]) and self.board[tmpX][tmpY] == 'o':
          surroundings[i][0][1] += 1
          tmpY += 1

        while cnt < 2 and tmpY < len(board[0]) and (self.board[tmpX][tmpY] == 'o' or self.board[tmpX][tmpY] == '.'):
          if self.board[tmpX][tmpY] == 'o':
            surroundings[i][1][1] += 1

          else:
            cnt += 1

          tmpY += 1

      elif i == 4:
        while tmpX < len(board) and tmpY < len(board[0]) and self.board[tmpX][tmpY] == 'o':
          surroundings[i][0][1] += 1
          tmpX += 1
          tmpY += 1

        while cnt < 2 and tmpX < len(board) and tmpY < len(board[0]) and (self.board[tmpX][tmpY] == 'o' or self.board[tmpX][tmpY] == '.'):
          if self.board[tmpX][tmpY] == 'o':
            surroundings[i][1][1] += 1

          else:
            cnt += 1

          tmpX += 1
          tmpY += 1
        
      elif i == 5:
        while tmpX < len(board) and self.board[tmpX][tmpY] == 'o':
          surroundings[i][0][1] += 1
          tmpX += 1

        while cnt < 2 and tmpX < len(board) and (self.board[tmpX][tmpY] == 'o' or self.board[tmpX][tmpY] == '.'):
          if self.board[tmpX][tmpY] == 'o':
            surroundings[i][1][1] += 1

          else:
            cnt += 1
            
          tmpX += 1

      elif i == 6:
        while tmpX < len(board) and tmpY >= 0 and self.board[tmpX][tmpY] == 'o':
          surroundings[i][0][1] += 1
          tmpX += 1
          tmpY -= 1

        while cnt < 2 and tmpX < len(board) and tmpY >= 0 and (self.board[tmpX][tmpY] == 'o' or self.board[tmpX][tmpY] == '.'):
          if self.board[tmpX][tmpY] == 'o':
            surroundings[i][1][1] += 1

          else:
            cnt += 1
            
          tmpX += 1
          tmpY -= 1
          
      elif i == 7:
        
        while tmpY >= 0 and self.board[tmpX][tmpY] == 'o':
          surroundings[i][0][1] += 1
          tmpY -= 1
          
        while cnt < 2 and tmpY >= 0 and (self.board[tmpX][tmpY] == 'o' or self.board[tmpX][tmpY] == '.'):
          if self.board[tmpX][tmpY] == 'o':
            surroundings[i][1][1] += 1

          else:
            cnt += 1
            
          tmpY -= 1
    
    return surroundings
      


        
        
