import game

if __name__ == "__main__":

   boardDim = int(input("Please input board dimension: "))

   game, curPlayer = Game(boardDim), 0

   while game.gameStatus:
      coord = list(input("Where would you like to place your next stone?: "))
      
      while not game.makeMove(curPlayer, coord):
         coord = list(input("Previous input was invalid. Please select a new coordinate: "))

      if game.gameStatus:
         curPlayer = (curPlayer + 1) % 2

   print(f"Congratulations! Player {curPlayer} has won the game!")
