class CycleDetection:
   
    def __init__(self):
        self.CycleDetection()
    
    # Return True if the current grid is in the history    
    def CycleDetection(self):
        from GameManager import GameManager
      
        grid = GameManager.GameOfLife
        history = GameManager.History
        
        currentAliveCellsList = GameManager.GetAliveCellsList(grid)
        
        for previousGrid in history:
            if len(currentAliveCellsList) == len(previousGrid):
                if self.ListEquals(currentAliveCellsList,previousGrid):
                    return True
        
        return False
    
    # Return True if both lists are the same
    def ListEquals (list1, list2):
        return list1 == list2