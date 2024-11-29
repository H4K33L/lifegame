import os
from random import choice

from CycleDetection import CycleDetection
from PrintGrid import PrintGrid
from NextStep import NextStep
from Save import Save
from Load import Load

class GameManager(object):
  Round = 0
  GameOfLife = []
  History = []
  CycleDetected = -1

  def __new__(game):
    if not hasattr(game, 'instance'):
      game.instance = super(GameManager, game).__new__(game)
    return game.instance
  
  def Start(self):
    caption = ""
    while (caption != "QUIT"):
      self.updateRound(0)
      self.updateCycleDetected()
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
  def updateCycleDetected(self) :
    self.CycleDetected = -1

  def SetGrid(self) :
    lenght = 0
    while not lenght:
        try:
            lenght = int(input('Chose the size : '))
            if 250 < lenght < 0 :
               raise ValueError
        except ValueError:
            lenght = 0
            print("That's not an option ! max value 250.")

    output = []
    for len in range(lenght) :
      line= []
      for height in range(lenght) :
        line.append(choice([0,1]))
      output.append(line)

    self.updateGameOfLife(output)

  @classmethod
  def updateGameOfLife(self, value) :
    self.GameOfLife = value
  
  @classmethod
  def updateHistory(self, value) :
    self.History.append(value)
    
  # Get the list of coordinates of all the alive cells from the grid
  def GetAliveCellsList(grid):
    aliveCellsList = []
    
    for row in range(len(grid)):
      for column in range(len(grid)):
        if grid[row][column] == 1:
          aliveCellsList.append((row,column))

    return aliveCellsList