# understand that the player who goes first is not allowed to make 3 x 3.


class Player:
  def __init__(self):
    self.placements = set()
    self.status = "pending"

class Game:
  def __init__(self, dim):
    self.player1 = Player()
    self.player2 = Player()
    self.board = [['.' for _ in range(dim)] for _ in range(dim)]

  def displayBoard(self):
    for row in self.board:
      print(row)

  def placeStone(self, player, x, y) -> list:
    # 

    if player == 2:


    if x >= len(self.board) or y >= len(self.board):
      print("This is an invalid placement. Please choose a different coordinate")
      return [False, 2]


    if (x, y) in self.player1.placements or (x, y) in self.player2.placements:
      print("This position has already been filled up. Please choose a different coordinate.")
      return [False, 2]


    if player == 0:
      self.player1.placements.add((x, y))


    else:
      self.player2.placements.add((x, y))


      self.board[x][y] = 'x'


      # check all eight directions surrounding the current placement


      surroundings = defaultdict(int)


      for i in range(8):
        tmpX, tmpY = x, y
        counter = 0

        if i == 0:
          while tmpX >= 0 and tmpY >= 0 and self.board[tmpX][tmpY] == 'x':
            counter += 1
            tmpX -= 1
            tmpY -= 1
       
        elif i == 1:
          while tmpX >= 0 and self.board[tmpX][tmpY] == 'x':
            counter += 1
            tmpX -= 1
       
        elif i == 2:
          while tmpX >= 0 and tmpY < len(board[0]) and self.board[tmpX][tmpY] == 'x':
            counter += 1
            tmpX -= 1
            tmpY += 1
       
        elif i == 3:
          while tmpY < len(board[0]) and self.board[tmpX][tmpY] == 'x':
            counter += 1
            tmpY += 1
       
        if i == 4:
          while tmpX < len(board) and tmpY < len(board[0]) and self.board[tmpX][tmpY] == 'x':
            counter += 1
            tmpX += 1
            tmpY += 1
       
        elif i == 5:
          while tmpX < len(board) and self.board[tmpX][tmpY] == 'x':
            counter += 1
            tmpX += 1
       
        elif i == 6:
          while tmpX < len(board) and tmpY >= 0 and self.board[tmpX][tmpY] == 'x':
            counter += 1
            tmpX += 1
            tmpY -= 1
       
        elif i == 7:
          while tmpY >= 0 and self.board[tmpX][tmpY] == 'x':
            counter += 1
            tmpY -= 1

      for i in range(4):
        if surroundings[i] + surroundings[i+4] - 1 >= 5:
          # case where white wins
          return [True, 2]
   
    return [True, 3]
