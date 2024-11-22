import json
import os

class Save :

    def InterfaceSave(self) :
        Name = input("enter a name : ")
        self.NewSave(Name)

    def NewSave(self, Name) :
        from GameManager import GameManager
        LastSave = []
        LastSave.append(GameManager.Round)
        LastSave.append(len(GameManager.GameOfLife))
        LastSave.append(GameManager.GetAliveCellsList(GameManager.GameOfLife))
        LastSaveJson = json.dumps(LastSave)
        File = open("save/"+Name+".json","x")
        File.write(LastSaveJson)
        File.close()

    def InterfaceLoad(self) :
        from GameManager import GameManager
        Files = os.listdir("/save")
        for i in range(Files) :
            print(i)
        content = ""
        while content not in Files :
            content = input("Enter Save name : " )
        File = open("save:"+content,"r")
        LoadSave = File.read()
        LastSave = json.loads(LoadSave)
        GameManager.updateRound(LastSave[0])
        Grid = self.GridRegen(LastSave[1], LastSave[2])
        GameManager.updateRound(Grid)

    def GridRegen(self, lenght, position) :
        Grid = []
        for i in range(lenght) :
            Line = []
            for j in range(lenght) :
                Line.append(0)
            Grid.append(Line)
        for coordonate in range(position) :
            Grid[coordonate[0]][coordonate[1]] = 1
        return Grid
