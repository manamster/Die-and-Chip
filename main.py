import playerClass
import boardClass

#Creation of the boardClass
board = boardClass.board()

def main(board):
  """Main function that runs all of the main game logic for each player as the game is being run it also displays the winner and the top scores at the end of a round"""
  winState = False
  turnNum = 1
  while winState != True:
    for player in board.getPlayerList():
      print("It is turn", turnNum)
      board.printBoard()
      player.playTurn()
      winState = player.checkWin()
      if winState == True:
        print(player, "won!")
        player.updateScores(turnNum) #Just need to fix this
        player.displayTopScores()
        break
    turnNum +=1

playAgain = "y"
while playAgain == "y":
  """This loops the main game logic along with the before logic such as creating players for the game. It also asks the user if they want to play again and loops if necessary."""
  print("\nWelcome to the Chip and Die game!\n")
  board.printInstructions()
  board.resetPlayerList()
  board.resetBoard()
  board.createPlayers(board)
  board.printPlayerOrder()
  main(board)
  tempVal = False
  while tempVal == False:
    try:
      playAgain = input("Would you like to play again? (y/n)\n").lower()
      if playAgain == "y" or playAgain == "n":
        tempVal = True
      else:
        tempVal = False
    except:
      print("That wasnt expected! Please answer with y or n")
      tempVal = False