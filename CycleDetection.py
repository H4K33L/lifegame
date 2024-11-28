class CycleDetection:
   
    def __init__(self):
        self.CycleDetection()
    
    # Return True if the current grid is in the history    
    def CycleDetection(self):
        from GameManager import GameManager
      
        grid = GameManager.GameOfLife
        history = GameManager.History
        
        currentAliveCellsList = GameManager.GetAliveCellsList(grid)
        
        for roundIndex in range(len(history)-1):
            if len(currentAliveCellsList) == len(history[len(history)-1-roundIndex]):
                if currentAliveCellsList == history[len(history)-1-roundIndex]:
                    GameManager.CycleDetected = len(history)-1-roundIndex