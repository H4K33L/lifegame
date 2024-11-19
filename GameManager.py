import os

from PrintGrid import printGrid

class GameManager(object):
  Round = 0
  GameOfLife = [[0,1,0],[1,0,1]]

  def __new__(game):
    if not hasattr(game, 'instance'):
      game.instance = super(GameManager, game).__new__(game)
    return game.instance
  
  def Start(self):
    #set grid
    caption = ""
    while (caption != "Q") :
      # calculate
      printGrid()
      caption = input()
      self.updateRound(self.Round + 1)
    
    os.system('cls')
  
  @classmethod
  def updateRound(self, value) :
    self.Round = value