import copy

class NextStep:
   
   def __init__(self):
      self.NextStep()

   def NextStep(self):
      """
      Calculate the next generation of cells based on the current grid state.
      
      This method applies the rules of Conway's Game of Life to determine which
      cells live, die, or are born in the next generation.
      """
      
      from GameManager import GameManager
      
      grid = GameManager.GameOfLife

      # Create a deep copy of the grid to store the next generation
      newgrid = copy.deepcopy(grid)
      
      # Get all alive cells from the grid
      aliveCellsList = GameManager.GetAliveCellsList(grid)
      deadCellsCheckedList = []
      
      for aliveCell in aliveCellsList:
         
         # Get the list of dead neighbors and the number of alive neighbors
         neighbors = self.GetNeighborCells(grid, aliveCell[0], aliveCell[1])
         nAliveNeighbors = neighbors[1]
         deadNeighborsList = neighbors[0]
          
         # Apply the survival rule: cell dies if it doesn't have 2 or 3 alive neighbors
         if nAliveNeighbors not in [2,3]:
            newgrid[aliveCell[0]][aliveCell[1]] = 0
         
         # Check all dead neighbors for potential birth
         for deadNeighbor in deadNeighborsList:
            if not deadNeighbor in deadCellsCheckedList:
               deadCellsCheckedList.append(deadNeighbor)
               sub_neighbors = self.GetNeighborCells(grid, deadNeighbor[0], deadNeighbor[1])
               sub_nAliveNeighbors = sub_neighbors[1]
            
               # Apply the birth rule: dead cell becomes alive if it has exactly 3 alive neighbors
               if sub_nAliveNeighbors == 3:
                  newgrid[deadNeighbor[0]][deadNeighbor[1]] = 1

      # Update the game history and current grid state
      GameManager.updateHistory(aliveCellsList)
      GameManager.updateGameOfLife(newgrid) 
   
   
   def GetNeighborCells(self, grid, row, column):
      """
      Get information about the neighboring cells of a given cell.

      Args:
         grid (list of lists): The current game grid.
         row (int): The row of the cell to check.
         column (int): The column of the cell to check.

      Returns:
         tuple: A tuple containing:
               - list: Coordinates of dead neighboring cells.
               - int: Number of alive neighboring cells.
      """
      
      # Define all possible neighbor positions
      neighbors = [(row-1,column-1),(row-1,column),(row-1,column+1),(row,column-1),(row,column+1),(row+1,column-1),(row+1,column),(row+1,column+1)]

      deadNeighborsList = []
      nAliveNeighbors = 0

      for neighborCell in neighbors:
         # Check if the neighbor is within grid boundaries
         if 0 <= neighborCell[0] < len(grid) and 0 <= neighborCell[1] < len(grid[0]):
            if grid[neighborCell[0]][neighborCell[1]] == 1:
               nAliveNeighbors += 1
            
            else:
               deadNeighborsList.append(neighborCell)
      
      return (deadNeighborsList, nAliveNeighbors)