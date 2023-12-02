# Author: Mihir Jain, Suraj S Bilgi
# Date: 25-11-2023
# Description: The Main code to start the Project

# Importing the GameEngine Class
from GameEngine import GameEngine

def main():
    game = GameEngine()

    game.initalizeGame()
    game.intro()
    remaining_veg = game.remainingVeggies()

    while remaining_veg > 0:
        print(f"Remaining Vegetables: {remaining_veg}")
        print(f"Player's Score: {game.getScore()}")
        game.printField()
        game.moveRabbits()
        game.moveCaptain()
        game.moveSnake()
        remaining_veg = game.remainingVeggies()

    game.gameOver()
    game.highScore()


if __name__ == "__main__":
    main()
