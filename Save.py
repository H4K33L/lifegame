import json

class Save:
    def __init__(self):
        self.InterfaceSave()
      
    def InterfaceSave(self):
        """
        input : None
        output : None
        This function just exist to take an user input and give
        it to the NewSave function.
        """
        # Prompt the user to enter a name for the save file
        Name = input("enter a name : ")
        self.NewSave(Name)

    def NewSave(self, Name):
        """
        input : Name a string
        output : None
        The function takes a string as input, and gets all information from
        the game manager instance to create a save of the actual game status.
        All the information are stocked in .json format (to be easily readable by the program).
        Do not panick the function anticipates if the Name.json file alredy exists, 
        the previosly named save just going to be overwrited.
        """
        from GameManager import GameManager
        
        # Create a list to store the save data, add the data then convert the save data list to a JSON string
        LastSave = []
        LastSave.append(GameManager.Round)
        LastSave.append(len(GameManager.GameOfLife))
        LastSave.append(GameManager.GetAliveCellsList(GameManager.GameOfLife))
        LastSaveJson = json.dumps(LastSave)
        
        # Open a file with the provided name and write the JSON string to the file
        File = open("saves/" + Name + ".json", "w")
        File.write(LastSaveJson)
        File.close()