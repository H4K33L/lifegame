import json
import os

class Load :

    def __init__(self):
        self.InterfaceLoad()

    def InterfaceLoad(self) :
        from GameManager import GameManager
        print("All Saved Games : ")
        Files = os.listdir("saves")
        for i in Files :
            print(i[:-5])
        content = ""
        while content+".json" not in Files :
            content = input("Enter Save name : " )
        File = open("saves/"+content+".json","r")
        LoadSave = File.read()
        File.close()
        LastSave = json.loads(LoadSave)
        GameManager.updateRound(LastSave[0])
        Grid = self.GridRegen(LastSave[1], LastSave[2])
        GameManager.updateGameOfLife(Grid)

    def GridRegen(self, lenght, position) :
        Grid = []
        for i in range(lenght) :
            Line = []
            for j in range(lenght) :
                Line.append(0)
            Grid.append(Line)
        for coordonate in position :
            Grid[coordonate[0]][coordonate[1]] = 1
        return Grid