import copy

class NextStep:
   
   def __init__(self):
      self.NextStep()

   def NextStep(self):
      from GameManager import GameManager
      
      grid = GameManager.GameOfLife

      newgrid = copy.deepcopy(grid)
      
      # Get all alive cells from the grid
      aliveCellsList = GameManager.GetAliveCellsList(grid)
      deadCellsCheckedList = []
      
      for aliveCell in aliveCellsList:
         
         # Get the list of dead neighbors and the number of alive neighbors
         neighbors = self.GetNeighborCells(grid, aliveCell[0], aliveCell[1])
         nAliveNeighbors = neighbors[1]
         deadNeighborsList = neighbors[0]
          
         # If there is not 2 or 3 alive neighbors then the cell dies
         if nAliveNeighbors not in [2,3]:
            newgrid[aliveCell[0]][aliveCell[1]] = 0
         
         #Checks all neighbors of the dead neighbor cells
         for deadNeighbor in deadNeighborsList:
            if not deadNeighbor in deadCellsCheckedList:
               deadCellsCheckedList.append(deadNeighbor)
               sub_neighbors = self.GetNeighborCells(grid, deadNeighbor[0], deadNeighbor[1])
               sub_nAliveNeighbors = sub_neighbors[1]
            
               # If there si 3 alive neighbors then the cell becomes alive
               if sub_nAliveNeighbors == 3:
                  newgrid[deadNeighbor[0]][deadNeighbor[1]] = 1

      GameManager.updateHistory(aliveCellsList)
      GameManager.updateGameOfLife(newgrid) 
   
   # Get the list of the coordinates of all the dead neighbor cells
   # Get the number of alive cells
   def GetNeighborCells(self, grid, row, column):
      neighbors = [(row-1,column-1),(row-1,column),(row-1,column+1),(row,column-1),(row,column+1),(row+1,column-1),(row+1,column),(row+1,column+1)]

      deadNeighborsList = []
      nAliveNeighbors = 0

      for neighborCell in neighbors:
         if 0 <= neighborCell[0] < len(grid) and 0 <= neighborCell[1] < len(grid[0]):
            if grid[neighborCell[0]][neighborCell[1]] == 1:
               nAliveNeighbors += 1
            
            else:
               deadNeighborsList.append(neighborCell)
      
      return (deadNeighborsList, nAliveNeighbors)