import os

class PrintGrid :

    def __init__(self):
        self.printgrid()

    def printgrid(self):
        from GameManager import GameManager
    
        os.system('cls')
        
        round = "Round " + str(GameManager.Round)
        lenght = len(GameManager.GameOfLife[0])
        height = len(GameManager.GameOfLife)

        print(round + "_"*(lenght*2-len(round)))

        for line in range(height) :
            lineContent = ""
            for column in range(lenght) :
                if GameManager.GameOfLife[line][column] == 0 :
                    lineContent += "░░"
                else :
                    lineContent += "██"
            print(lineContent)

        print("type Q to quit, S to save, L to load or press Enter.")

