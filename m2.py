from ge2 import GameEngine


def main():

    game = GameEngine()

    game.initalizeGame()
    game.intro()
    remaining_veg = game.remainingVeggies()

    # while remaining_veg:
    print(f"Remaining Vegetables: {remaining_veg}")
    print(f"Player's Score: {game.getScore()}")
    game.printField()
    game.moveRabbits()


if __name__ == "__main__":
    main()
