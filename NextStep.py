class NextStep:
   
   def __init__(self, grid):
      self.NextStep(self, grid)

   def NextStep(self, grid):
      
      newgrid = grid
      
      # Get all alive cells from the grid
      aliveCellsList = self.GetAliveCellsList(self, grid)
      
      for aliveCell in aliveCellsList:
         
         # Get the list of dead neighbors and the number of alive neighbors
         neighbors = self.GetNeighborCells(self, grid, aliveCell[0], aliveCell[1])
         nAliveNeighbors = neighbors[1]
         deadNeighborsList = neighbors[0]
          
         # If there is not 2 or 3 alive neighbors then the cell dies
         if nAliveNeighbors not in [2,3]:
            newgrid[aliveCell[0]][aliveCell[1]] == 0
         
         #Checks all neighbors of the dead neighbor cells
         for deadNeighbor in deadNeighborsList:
            sub_neighbors = self.GetNeighborCells(self, grid, deadNeighbor[0], deadNeighbor[1])
            sub_nAliveNeighbors = sub_neighbors[1]
            
            # If there si 3 alive neighbors then the cell becomes alive
            if sub_nAliveNeighbors == 3:
               newgrid[deadNeighbor[0]][deadNeighbor[1]] == 1
   
      return newgrid      
   
   
   # Get all alive cells from the grid     
   def GetAliveCellsList(self, grid):
      aliveCellsList = []
    
      for i in range(len(grid)):
         for j in range(len(grid)):
            if grid[i][j] == 1:
               aliveCellsList.append((i,j))

      return aliveCellsList
   
   
   # Get the list of the coordinates of all the dead neighbor cells
   # Get the number of alive cells
   def GetNeighborCells(self, grid, x, y):
      neighbors = [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]

      deadNeighborsList = []
      nAliveNeighbors = 0

      for neighborCell in neighbors:
         if 0 <= neighborCell[0] < len(grid) and 0 <= neighborCell[1] < len(grid):
            if grid[neighborCell[0]][neighborCell[1]] == 1:
               nAliveNeighbors += 1
            
            else:
               deadNeighborsList.append(neighborCell)
      
      return (deadNeighborsList, nAliveNeighbors)