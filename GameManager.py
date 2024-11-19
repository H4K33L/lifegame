class GameManager(object):
  GameOfLife = []

  def __new__(game):
    if not hasattr(game, 'instance'):
      game.instance = super(GameManager, game).__new__(game)
    return game.instance
  
  def Start(self):
    print("start")