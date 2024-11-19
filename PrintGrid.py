from GameManager.py import game

class printGrid :

    def __init__(self):
        self.printgrid()

    def printgrid(self):
        round = "Round " + game.getRound
        lenght = len(game.getGrid[0])
        height = len(game.getGrid)

        print(round + "_"*(lenght-len(round)))

        for line in range(height) :
            lineContent = ""
            for column in range(lenght) :
                if game.getGrid[line][column] == 0 :
                    lineContent += chr(219)
                else :
                    lineContent += game.getGrid[line][column]
            print(lineContent)


        print("type Q to quit or press Enter.")

