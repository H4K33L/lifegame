import json
import os

class Load :

    def __init__(self):
        self.InterfaceLoad()

    def InterfaceLoad(self) :
        from GameManager import GameManager
        Files = os.listdir("save")
        for i in Files :
            print(i)
        content = ""
        while content not in Files :
            content = input("Enter Save name : " )
        File = open("save/"+content,"r")
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