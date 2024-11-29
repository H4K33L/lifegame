class CycleDetection:
   
    def __init__(self):
         # Constructor calls the CycleDetection method upon instantiation
        self.CycleDetection()
    
    # Method to detect cycles in the Game of Life
    # If a match is found, set the CycleDetected attribute to the round where the cycle was detected
    def CycleDetection(self):
        from GameManager import GameManager
      
        grid = GameManager.GameOfLife
        history = GameManager.History

        currentAliveCellsList = GameManager.GetAliveCellsList(grid)
        
        # Iterate through the history in reverse order (from the most recent to the oldest)
        for roundIndex in range(len(history)-1):
            
            # Calculate the actual index in history we're comparing
            historyIndex = len(history) - 1 - roundIndex
            
            # checks if the number of alive cells matches, then if all the alive cells matches
            if len(currentAliveCellsList) == len(history[historyIndex]):
                if currentAliveCellsList == history[historyIndex]:
                    GameManager.CycleDetected = historyIndex