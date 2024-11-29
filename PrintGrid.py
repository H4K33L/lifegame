import os

class PrintGrid:
    def __init__(self):
        """
        input : None
        output : None
        Initialize the PrintGrid object and call the printgrid method
        """ 
        self.printgrid()

    def printgrid(self):
        """
        input : None
        output : None
        The function print the game interface.
        """ 
        from GameManager import GameManager

        # Clear terminal
        os.system('cls' if os.name == 'nt' else 'clear')

        # Prepare the round number string
        round = "Round " + str(GameManager.Round)
        lenght = len(GameManager.GameOfLife[0])
        height = len(GameManager.GameOfLife)

        # Print the game interface
        print(" " + round + "▁"*(lenght*3-len(round)))
        for line in range(height):
            lineContent = ""
            for column in range(lenght):
                if GameManager.GameOfLife[line][column] == 0:
                    lineContent += "\033[7m███\033[0m"
                else:
                    lineContent += "███"
            print("▕"+ lineContent + "▏")
        print(" "+ "▔"*(lenght*3))
        
        # If a cycle is detected, print the round number when it was detected also say since the game is ended
        if GameManager.CycleDetected != -1:
            if GameManager.GetAliveCellsList(GameManager.GameOfLife) != [] :
                print("Cycle detected since round " + str(GameManager.CycleDetected))
            else :
                print("Game ended since round " + str(GameManager.CycleDetected))

        # Print instructions for user input
        print("type Q to quit, S to save, L to load or press Enter.")