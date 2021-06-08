import dieClass
import time
import os
import json

class player(object):
  def __init__(self, board, name, startingChips = 5):
    """Hold values needed for each player"""
    self.numChips = startingChips
    self.numTurns = 0
    self.die = dieClass.Die(6)
    self.board = board
    self.name = name
    self.rollIR()
    
  def rollIR(self):
    """Rolls the initial roll and can be recalled if the roll is equal to another player's roll"""
    self.initialRoll = self.die.roll()

  def getIR(self):
    """Gets the initial roll for the addPlayers function so that it can sort the players by their rolls"""
    return(self.initialRoll)
  
  def compareTo(self, otherPlayer):
    """Used for sorting the players by returning values based on others players initial rolls"""
    if self.initialRoll > otherPlayer.getIR():
      return(1)
    elif self.initialRoll < otherPlayer.getIR():
      return(-1)
    else:
      return(0)

  def setSpace(self, num):
    """Sets each space based on wether the dice was rolled for that space and if it has a chip or not"""
    tempVar = False
    if num == 1:
      tempVar = self.getSpace(num)
      if tempVar == True:
        self.numChips += 1
        self.board.setS1(0)
      else:
        self.numChips -= 1
        self.board.setS1(1)
    elif num == 2:
      tempVar = self.getSpace(num)
      if tempVar == True:
        self.numChips += 1
        self.board.setS2(0)
      else:
        self.numChips -= 1
        self.board.setS2(1)
    elif num == 3:
      tempVar = self.getSpace(num)
      if tempVar == True:
        self.numChips += 1
        self.board.setS3(0)
      else:
        self.numChips -= 1
        self.board.setS3(1)
    elif num == 4:
      tempVar = self.getSpace(num)
      if tempVar == True:
        self.numChips += 1
        self.board.setS4(0)
      else:
        self.numChips -= 1
        self.board.setS4(1)
    elif num == 5:
      tempVar = self.getSpace(num)
      if tempVar == True:
        self.numChips += 1
        self.board.setS5(0)
      else:
        self.numChips -= 1
        self.board.setS5(1)
    else:
      #This else statement is for #6 and it just subtracts a player chip and adds to the space
      self.numChips -= 1
      self.board.addS6()

  def getSpace(self, num):
    """Gets the spaces from the board for the chip check for setting them above"""
    tempVar = 0
    if num == 1:
      tempVar = self.board.getS1()
      if tempVar == 1:
        return(True)
    elif num == 2:
      tempVar = self.board.getS2()
      if tempVar == 1:
        return(True)
    elif num == 3:
      tempVar = self.board.getS3()
      if tempVar == 1:
        return(True)
    elif num == 4:
      tempVar = self.board.getS4()
      if tempVar == 1:
        return(True)
    else:
      tempVar = self.board.getS5()
      if tempVar == 1:
        return(True)
    return(False)

  def playTurn(self):
    """Runs all the previous game based code and prompts the user for input. It also increments the number of turns and tells the user what turn it is and how many chips they have left along with paying the dice roll animation"""
    print(self.name, end=" ")
    input("press enter to roll.\n")
    roll = self.die.roll()
    self.animation(roll)
    print(self.name,"rolled a", str(roll), "\n")
    self.setSpace(roll)
    print(self.name,"has", str(self.numChips), "chips left.")
    self.numTurns += 1


  def animation(self, rollNum):
    """Plays the animation for rolling the dice and then it displays what you got."""
    for i in range(0,4):
      os.system("clear")
      print("""
_________
|       |
|   .   |
|       |
---------
      """)
      time.sleep(0.1)
      os.system("clear")
      print("""
_________
|   .   |
|       |
|   .   |
---------      
      """)
      time.sleep(0.1)
      os.system("clear")
      print("""
_________
|   .   |
|   .   |
|   .   |
---------      
      """)
      time.sleep(0.1)
      os.system("clear")
      print("""
_________
|  .  . |
|       |
|  .  . |
---------      
      """)
      time.sleep(0.1)
      os.system("clear")
      print("""
_________
|  .  . |
|   .   |
|  .  . |
---------      
      """)
      time.sleep(0.1)
      os.system("clear")
      print("""
_________
|  .  . |
|  .  . |
|  .  . |
---------      
      """)
      time.sleep(0.1)
      os.system("clear")
    if rollNum == 1:
      print("""
_________
|       |
|   .   |
|       |
---------
      """)
    elif rollNum == 2:
      print("""
_________
|   .   |
|       |
|   .   |
---------      
      """)
    elif rollNum == 3:
      print("""
_________
|   .   |
|   .   |
|   .   |
---------      
      """)
    elif rollNum == 4:
      print("""
_________
|  .  . |
|       |
|  .  . |
---------      
      """)
    elif rollNum == 5:
      print("""
_________
|  .  . |
|   .   |
|  .  . |
---------      
      """)
    else:
      print("""
_________
|  .  . |
|  .  . |
|  .  . |
---------      
      """)
  
  def __str__(self):
    """Str function used for getting names when printing players order"""
    return(self.name)
  
  def checkWin(self):
    """Checks at the end of each turn as to if the user has won the game by having zero chips. No need for a negative chip check since it is impossible for a player to lose more than 1 chip per turn"""
    if self.numChips == 0:
      return(True)

  def updateScores(self, turnNum):
    """Grabs the list of the top 5 scores from the json file and adds the current score for this winning round to it. Then it sorts the list from low to high and cuts off the 6th value so it always will have 5 top scores. It then rewrites the changes to the json file."""
    addScore = [self.name, int(self.numTurns)]
    try:
      file = open("topScores.json","r")
      scoresList = json.load(file)
      file.close()
    except:
      scoresList = [["Calvin",7],["Mimi",9],["Hayes",10],["Julie",11],["Katie",18]]
      file = open("topScores.json", "w")
      json.dump(scoresList,file)
      file.close()
    lenList = len(scoresList)
    scoresList.insert(0,addScore) #Have to put the score at the beginning with insert or the bubble sort wont work
    #Bubble sort cause nested lists cant be sorted easily
    for i in range(lenList):
      for j in range(0,lenList-i-1):
        if scoresList[j][1] > scoresList[j+1][1]:
          scoresList[j], scoresList[j+1] = scoresList[j+1], scoresList[j]
    del scoresList[5] #This always deletes the 6th thing on this list which is the highest number since we just sorted it. This keeps the list at 5 people long
    file = open("topScores.json", "w")
    json.dump(scoresList, file)
    file.close()
  
  def displayTopScores(self):
    """Grabs the json file in read mode and displays the top scores in the order they are in in the json file (which is low to high because of the function above)"""
    print("Top Scores.")
    file = open("topScores.json","r")
    scoresList = json.load(file)
    for i in range(len(scoresList)):
      print(str(i+1) + ".",scoresList[i][0],"\t",scoresList[i][1],"turns")
    file.close()
