import json

class Save :

    def __init__(self):
        self.InterfaceSave()
      
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