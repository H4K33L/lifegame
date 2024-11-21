class NextStep:
   
   def __init__(self, grid):
      self.NextStep(self, grid)

   def NextStep(self, grid):
      newgrid = grid
      aliveCellsList = self.GetAliveCellsList(self.grid)
      for aliveCell in aliveCellsList:
         neighbors = self.GetNeighborCells(self, grid, aliveCell[0], aliveCell[1])
         nAliveNeighbors = 0
         for neighbor in neighbors:
            if grid[neighbor[0]][neighbor[1]] == 1:
               nAliveNeighbors += 1
         if nAliveNeighbors not in [2,3]:
            newgrid[aliveCell[0]][aliveCell[1]] == 0
         
             
            
          
          
   def GetAliveCellsList(self, grid):
      aliveCellsList = []
    
      for i in range(len(grid)):
         for j in range(len(grid)):
            if grid[i][j] == 1:
               aliveCellsList.append((i,j))

      return aliveCellsList
    
   def GetNeighborCells(self, grid, x, y):
      neighbors = [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]

      validNeighbors = []

      for neighborCell in neighbors:
         if 0 <= neighborCell[0] < len(grid) and 0 <= neighborCell[1] < len(grid):
            validNeighbors.append(neighborCell)
      
      return validNeighbors