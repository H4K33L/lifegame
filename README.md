# Conway's Game Of Life

Description
------------
This project implements Conway's Game of Life, a cellular automaton simulation. The game is played on an n x n grid where each cell is either alive or dead. The state of each cell in the next generation is determined by its current state and the states of its eight neighbors. We also implemented a cycle detection method, Once a cycle is detected you will know the round when it started.

### Installation

* Step 1: Make sure you have **Python3** or higher installed
* Step 2: in your terminal, enter : ```python3 main.py```

### Usage

#### In the Main Menu:
* Enter ```L``` to **load** saved game.
  * Every saved games in the 'saves' folder will be shown.
  * You will have to enter the name of the game. 
* Enter ```QUIT``` to **close** the program.
* Enter anything else to start a new game:
  * You will be promted to choose the grid size between 1 by 1 and 250 by 250.

#### In the game:
* Enter ```Q``` to **quit** the current game **Without saving the game**.
* Enter ```S``` to **save** the current game.
  * If you save the game under an **existing game**'s name, it will be **overwriten** by the current game.
  * If you enter a new game name, it will create a new .json file in the 'saves' folder.
  * You can then continue to play the game or choose to Quit or Load a new game.
* Enter ```L``` to **load** a new saved game **Without saving the game**.
* Enter anything else to calculate and show the next step of the game:

## Game of Life Rules
- A dead cell with exactly 3 live neighbors becomes alive.
- A live cell with 2 or 3 live neighbors stays alive.
- All other live cells die, and all other dead cells stay dead.

### Additional Resources

* What is Conway's Game of Life: [Wikipedia](https://en.wikipedia.org/wiki/Conway's_Game_of_Life)
* Game Of Life Simulator: [Experiment with Conway's Game of Life](https://www.dcode.fr/jeu-de-la-vie)

### Authors

* Jeremy Gaudin
* Kelyan Danis
* Remy Portier
