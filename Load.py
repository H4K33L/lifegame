import json
import os

class Load:
    def __init__(self):
        """
        input : None
        output : None
        Initialize the Load object and call the InterfaceLoad method
        """ 
        self.InterfaceLoad()

    def InterfaceLoad(self):
        from GameManager import GameManager
        
        # List all files in the "saves" directory and let the let the user chose with he would open
        print("All Saved Games : ")
        Files = os.listdir("saves")
        for i in Files:
            print(i[:-5])
        content = ""
        while content + ".json" not in Files:
            content = input("Enter Save name: ")
        
        # Open and read the selected save file
        File = open("saves/" + content + ".json", "r")
        LoadSave = File.read()
        File.close()
        
        # Parse the JSON content of the save file and add it to the Gamanager instance
        LastSave = json.loads(LoadSave)

        # Error cases
        if 3 != len(LastSave):
            GameManager.updateRound(0)
            GameManager.updateGameOfLife([[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,1,1,0,0,1,1,0,0],[0,0,1,1,0,0,1,1,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]])
        else:
            GameManager.updateRound(LastSave[0])
            Grid = self.GridRegen(LastSave[1], LastSave[2])
            GameManager.updateGameOfLife(Grid)

    def GridRegen(self, length, position):
        """
        Input : length an int, position a array of tuples
        output : Grid an aray of array fill by 1 and 0
        This function
        """

        # Error case, if a stupid user try to be a fool
        if not 251 > length > 0 :
            return [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        elif len(position) > length*length :
            return [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0,0],[0,0,0,1,0,1,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
        for cordinate in position :
            if cordinate[0] < 0 or cordinate[0] > length-1 or cordinate[1] < 0 or cordinate[1] > length-1 :
                return [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,1,0,0],[0,0,0,1,0,0,1,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[0,0,0,1,0,0,1,0,0,0],[0,0,1,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
        # Regenerate the grid based on saved length and alive cell positions
        Grid = []
        for i in range(length):
            Line = []
            for j in range(length):
                Line.append(0)  
            Grid.append(Line)
        for coordinate in position:
            Grid[coordinate[0]][coordinate[1]] = 1
        
        return Grid