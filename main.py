import game
from collections import defaultdict

if __name__ == "__main__":

   boardDim = int(input("Please input board dimension: "))

   game, curPlayer = game.Game(boardDim), 0

   while game.gameStatus:
      # during the current player's turn, if the revert button were to be pressed, this
      # means that the previous player would like to take his turn back... thus,
      # we would be dealing with the previous player and it would now be the previous
      # player's turn

      # during each turn, there are two choices
        # 1) current player places their stone
        # 2) previous player takes back his stone and chooses
        #    to place it on a different spot.

      # ask whether they would like to place or the previous player would like to go
      # back and change his placement

      action = input(f"Player {curPlayer + 1}. Place your stone or previous player removes their most recent stone (place or remove): ")

      if action == "place":
        coord = (input(f"Player {curPlayer + 1}'s turn. Where would you like to place your next stone?: ")).split()

        coord = tuple([int(i) for i in coord])
        
        while not game.makeMove(curPlayer, coord):
          coord = (input("Previous placement was invalid. Choose a new position: ")).split()
          coord = tuple([int(i) for i in coord])

        if game.gameStatus:
          curPlayer = (curPlayer + 1) % 2

      else:
        # we do not take a coordinate
        curPlayer = (curPlayer + 1) % 2
        tof = game.removeStone(curPlayer)

        if not tof:
          curPlayer = (curPlayer + 1) % 2

      game.gameBoard.displayBoard()

    # defaultdict(<class 'list'>, {0: [1, 0], 1: [2, 0], 2: [1, 0], 3: [2, 0], 4: [1, 0], 5: [2, 0], 6: [1, 0], 7: [2, 0]})
    # (5,5) -> (4,6) -> (4,4) -> (3,5) -> (4,5)

   print(f"Congratulations! Player {curPlayer + 1} has won the game!")
