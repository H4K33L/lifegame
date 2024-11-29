import os
from random import choice

from CycleDetection import CycleDetection
from PrintGrid import PrintGrid
from NextStep import NextStep
from Save import Save
from Load import Load

class GameManager(object):
  """Manages the Game of Life simulation."""
  Round = 0
  GameOfLife = []
  History = []
  CycleDetected = -1

  def __new__(game):
    # Singleton pattern implementation
    if not hasattr(game, 'instance'):
      game.instance = super(GameManager, game).__new__(game)
    return game.instance
  
  def Start(self):
    """Main game loop."""
    caption = ""
    while (caption != "QUIT"):
      self.updateRound(0)
      self.resetCycleDetected()
      self.resetHistory()
      os.system('cls' if os.name == 'nt' else 'clear')
      caption = input("Press L to load a game | Press enter to start a new game | Enter QUIT to close the program : ")
      if caption == "L":
        Load()
        caption = ""
      elif caption == "QUIT":
        break
      else :
        self.SetGrid()
        caption = ""

      while (caption != "Q"):
        PrintGrid()
        caption = input()
        if caption == "S":
          Save()
        elif caption == "L":
          Load()
        elif caption == "Q":
          break
        else :
          self.updateRound(self.Round + 1)
          NextStep()
          if self.CycleDetected == -1:
            CycleDetection()
      
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Program succesfully closed")
  
  @classmethod
  def updateRound(self, value) :
    self.Round = value

  @classmethod
  def resetCycleDetected(self) :
    self.CycleDetected = -1
    
  @classmethod
  def resetHistory(self) :
    self.History = []

  @classmethod
  def updateGameOfLife(self, value) :
    self.GameOfLife = value
  
  @classmethod
  def updateHistory(self, value) :
    self.History.append(value)
    
  def SetGrid(self) :
    """Initialize the game grid."""
    length = 0
    while not length:
        try:
            length = int(input('Chose the size : '))
            if not 251 > length > 0  :
               raise ValueError
        except ValueError:
            length = 0
            print("That's not an option ! max value 250.")

    # Generate random grid
    output = [[choice([0,1]) for _ in range(length)] for _ in range(length)]

    self.updateGameOfLife(output)

    
  def GetAliveCellsList(grid):
    """Return list of coordinates of all alive cells."""
    aliveCellsList = []
  
    for row in range(len(grid)):
      for column in range(len(grid)):
        if grid[row][column] == 1:
          aliveCellsList.append((row,column))

    return aliveCellsList