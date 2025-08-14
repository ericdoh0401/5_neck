import game
from collections import defaultdict

if __name__ == "__main__":

   boardDim = int(input("Please input board dimension: "))

   game, curPlayer = game.Game(boardDim), 0

   while game.gameStatus:
      coord = (input(f"Player {curPlayer + 1}'s turn. Where would you like to place your next stone?: ")).split()

      coord = tuple([int(i) for i in coord])
      
      while not game.makeMove(curPlayer, coord):
         coord = (input("Previous placement was invalid. Choose a new position: ")).split()
         coord = tuple([int(i) for i in coord])

      if game.gameStatus:
         curPlayer = (curPlayer + 1) % 2

      game.gameBoard.displayBoard()

   print(f"Congratulations! Player {curPlayer + 1} has won the game!")
