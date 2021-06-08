import os
import time
import playerClass

class board(object):
  def __init__(self):
    """Creates the spaces on the board"""
    self.space1 = 0
    self.space2 = 0
    self.space3 = 0
    self.space4 = 0
    self.space5 = 0
    self.space6 = 0
    self.playerList = []
  def getS1(self):
    """Gets Space 1"""
    return(self.space1)

  def setS1(self, num):
    """Sets space 1. Used for the player to take and place chips"""
    self.space1 = num

  def getS2(self):
    """Gets Space 2"""
    return(self.space2)

  def setS2(self, num):
    """Sets space 2. Used for the player to take and place chips"""
    self.space2 = num

  def getS3(self):
    """Gets Space 3"""
    return(self.space3)

  def setS3(self, num):
    """Sets space 3. Used for the player to take and place chips"""
    self.space3 = num

  def getS4(self):
    """Gets Space 4"""
    return(self.space4)
  
  def setS4(self, num):
    """Sets space 4. Used for the player to take and place chips"""
    self.space4 = num

  def getS5(self):
    """Gets Space 5"""
    return(self.space5)
  
  def setS5(self, num):
    """Sets space 5. Used for the player to take and place chips"""
    self.space5 = num

  def getS6(self):
    """Gets Space 6"""
    return(self.space6)

  def addS6(self):
    """Adds to space 6 since none can be taken from this space."""
    self.space6 += 1

  def printBoard(self):
    """Prints the board with formatting and prints the states of each space along with its space number"""
    print("""
Space 1   Space 2   Space 3   Space 4   Space 5   Space 6
-------   -------   -------   -------   -------   -------""")
    print("{:>4}{:>10}{:>10}{:>10}{:>10}{:>10}".format(str(self.space1), str(self.space2), str(self.space3), str(self.space4), str(self.space5), str(self.space6)))
    print()
  
  def addPlayers(self, player):
    """Adds the players to a list and sorts them by who had the lowest initial dice rolls and if there are people who had the same dice roll it returns a false which gets the main client code to prompt the player class to reroll its initial roll"""
    if len(self.playerList) == 0:
      self.playerList.append(player)
    else:
      i = 0
      for item in self.playerList:
        if player.compareTo(item) == -1:
          self.playerList.insert(i,player)
          return(True)
        elif player.compareTo(item) == 0:
          player.rollIR()
          return(False)
        elif player.compareTo(item) == 1 and item == self.playerList[len(self.playerList) - 1]:
          self.playerList.insert(i + 1,player)
          return(True)
        i += 1

  def getPlayerList(self):
    """Gets the player list"""
    return(self.playerList)

  def resetPlayerList(self):
    """Resets the player list"""
    self.playerList = []
  
  def printPlayerOrder(self):
    """Prints the player order in the order that they roll the dice during the game."""
    print("The order of players is ...")
    print()
    for i in range(len(self.playerList)):
      print("\t" + str(i+1) + ".", end = "   ")
      print(self.playerList[i])
    print()
  
  def createPlayers(self, board):
    """Creates 6 seperate instances of player classes and then adds them to the list one at a time. Also querries the user for all the info needed about the number of players and what the name of each player is."""
    tempVar = 0
    while tempVar == 0:
      try:
        numPlayers = int(input("How many players do you want to have?\n"))
        if numPlayers >= 2 and numPlayers <= 6:
          tempVar = 1
        else:
          print("Thats not the right amount of players please have 2-6 players.")
      except:
        print("That number wont work please enter a number between 2 and 6.")

    for i in range(numPlayers):
      tempState = False
      os.system('clear')
      name = input("What is the name of player " + str(i + 1) + "?\n")
      if i == 0:
        player1 = playerClass.player(board, name)
        while tempState == False:
          print(player1, "has an initial roll of", player1.getIR(), "\n")
          time.sleep(0.1)
          tempState = self.addPlayers(player1)
          if tempState == False:
            print("Thats a tie. Rerolling ...\n")
            time.sleep(0.5)
            os.system('clear')
          else:
            input("Press enter to continue")
      elif i == 1:
        player2 = playerClass.player(board, name)
        while tempState == False:
          print(player2, "has an initial roll of", player2.getIR(), "\n")
          time.sleep(0.1)
          tempState = self.addPlayers(player2)
          if tempState == False:
            print("Thats a tie. Rerolling ...\n")
            time.sleep(0.5)
            os.system('clear')
          else:
            input("Press enter to continue")
      elif i == 2:
        player3 = playerClass.player(board, name)
        while tempState == False:
          print(player3, "has an initial roll of", player3.getIR(), "\n")
          time.sleep(0.1)
          tempState = self.addPlayers(player3)
          if tempState == False:
            print("Thats a tie. Rerolling ...\n")
            time.sleep(0.5)
            os.system('clear')
          else:
            input("Press enter to continue")
      elif i == 3:
        player4 = playerClass.player(board, name)
        while tempState == False:
          print(player4, "has an initial roll of", player4.getIR(), "\n")
          time.sleep(0.1)
          tempState = self.addPlayers(player4)
          if tempState == False:
            print("Thats a tie. Rerolling ...\n")
            time.sleep(0.5)
            os.system('clear')
          else:
            input("Press enter to continue")
      elif i == 4:
        player5 = playerClass.player(board, name)
        while tempState == False:
          print(player5, "has an initial roll of", player5.getIR(), "\n")
          time.sleep(0.1)
          tempState = self.addPlayers(player5)
          if tempState == False:
            print("Thats a tie. Rerolling ...\n")
            time.sleep(0.5)
            os.system('clear')
          else:
            input("Press enter to continue")
      elif i == 5:
        player6 = playerClass.player(board, name)
        while tempState == False:
          print(player6, "has an initial roll of", player6.getIR(), "\n")
          time.sleep(0.1)
          tempState = self.addPlayers(player6)
          if tempState == False:
            print("Thats a tie. Rerolling ...\n")
            time.sleep(0.5)
            os.system('clear')
          else:
            input("Press enter to continue")
  
  def resetBoard(self):
    """Resets all values on the board to zero"""
    self.space1 = 0
    self.space2 = 0
    self.space3 = 0
    self.space4 = 0
    self.space5 = 0
    self.space6 = 0

  def printInstructions(self):
    """Prints the instructions for the game at the beginning of each game."""
    print("""•	Aim of the Game is to be the first to lose all of your chips
•	Players are put in order of the lowest to 
highest based on their first roll
(This is done automatically when you enter your name)
• You start out with 5 chips.
• When it is your turn you roll the die.
\t•	If the space with the same number as the die is empty (value of 0),
\t\tput a chip there.
\t•	but if there already is a chip there (value of 1), you must take it.
\t•	If you roll a 6, you always put one of your chips on the space number 6 – 
\t\tregardless of how many chips are there already. 
\t\tChips on space number 6 are out of the game,
\t\tand you never pick these up again.
""")