import random
class Die:
    """Class to make a die and roll it to evaluate the numbers"""

    def __init__(self, side):
        """Constructor of die. Sets side."""
        self.currentSide = 1
        self.sides = side
        
    def getFaceValue(self):
        """Returns what side the dice is on"""
        return self.currentSide
        
    def getNumberofSides(self):
        """Returns number of sides"""
        return self.sides

    def roll(self):
        """Rolls the dice"""
        self.currentSide = random.randrange(1,self.sides +1)
        return self.currentSide
    
    def __str__(self):
      """Returns the dice with the number of sides it has"""
      return("\nI am a dice with " + str(self.sides) + " sides and am currently on the " +str(self.currentSide) + " side.")