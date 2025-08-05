class Player1:
  def __init__(self):
    self.placements = set()

  def blackSurroundings(self, coord):

    surroundings = defaultdict(list)
    
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
      


        
        
