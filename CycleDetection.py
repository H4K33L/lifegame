class CycleDetection:
   
    def __init__(self):
        self.CycleDetection()
    
    # Return True if the current grid is in the history    
    def CycleDetection(self):
        from GameManager import GameManager
      
        grid = GameManager.GameOfLife
        history = GameManager.History
        
        currentAliveCellsList = GameManager.GetAliveCellsList(grid)
        
        for roundIndex  in range(len(history)):
            if len(currentAliveCellsList) == len(history[roundIndex]):
                for cellIndex in range(len(history[roundIndex])):
                    if currentAliveCellsList[cellIndex]!=history[roundIndex][cellIndex]:
                        break
                return roundIndex        
                        
        return -1
    
    # Return True if both lists are the same
    def ListEquals (self, list1, list2):
        return list1 == list2