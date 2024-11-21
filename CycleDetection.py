class CycleDetection:
   
    def __init__(self, grid, history):
        self.CycleDetection(self, grid, history)
    
    # Return True if the current grid is in the history    
    def CycleDetection(self, grid, history):
        currentAliveCellsList = self.GetAliveCellsList(grid)
        for previousGrid in history:
            if len(currentAliveCellsList) == len(previousGrid):
                if self.ListEquals(currentAliveCellsList,previousGrid):
                    return True
        return False
    
    # Return True if both lists are the same
    def ListEquals (list1, list2):
        return list1 == list2
    
    # Get all alive cells from the grid     
    def GetAliveCellsList(self, grid):
        aliveCellsList = []
    
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1:
                    aliveCellsList.append((i,j))
                    
        return aliveCellsList