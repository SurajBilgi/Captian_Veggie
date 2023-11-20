
import os
import pickle
import random
from Captain import Captain
from FieldInhabitant import FieldInhabitant
from Rabbit import Rabbit

from Veggie import Veggie


class GameEngine:
    NUMBEROFVEGGIES = 30
    NUMBEROFRABBITS = 5
    HIGHSCOREFILE = 'highscore.data'

    def __init__(self):
        self.field = []
        self.rabbits = []
        self.captain = None
        self.possible_veggies = []
        self.score = 0

    def init_veggies(self):
        import os
        filename = input("Enter the name of the file: ")
        try:
            while not os.path.exists(filename):
                filename = input(
                    "That file does not exist! Please enter the name of the file :")

            with open(filename, 'r') as file:
                dimensions = file.readline().strip().split(',')
                rows, cols = int(dimensions[1]), int(dimensions[2])
                self.field = [[None for _ in range(cols)] for _ in range(rows)]

                for line in file:
                    veg = line.strip().split(',')
                    name, symbol, points = veg[0], veg[1], int(veg[2])
                    self.possible_veggies.append(Veggie(name, symbol, points))

                added_veggies = 0
                while added_veggies < self.NUMBEROFVEGGIES:
                    row = random.randint(0, rows-1)
                    col = random.randint(0, cols-1)

                    if self.field[row][col] is None:
                        self.field[row][col] = self.possible_veggies[random.randint(
                            0, len(self.possible_veggies) - 1)]
                        added_veggies += 1
                        print(
                            f"Veggie added at ({row}, {col}) - Total: {added_veggies}/{self.NUMBEROFVEGGIES}")

        except Exception as e:
            print("Exception ", str(e))
            return -1

    def init_captain(self):
        rows, cols = len(self.field), len(self.field[0])
        while True:
            random_row = random.randint(0, rows-1)
            random_col = random.randint(0, cols-1)
            if self.field[random_row][random_col] is None:
                self.captain = Captain(random_row, random_col)
                self.field[random_row][random_col] = self.captain

                print(f"Captain added at ({random_row}, {random_col})")

                break

    def init_Rabbits(self):
        rows, cols = len(self.field), len(self.field[0])
        added_rabbits = 0
        while added_rabbits < self.NUMBEROFRABBITS:
            random_row = random.randint(0, rows-1)
            random_col = random.randint(0, cols-1)
            if self.field[random_row][random_col] is None:
                rabbit = Rabbit(random_row, random_col)
                self.rabbits.append(rabbit)
                self.field[random_row][random_col] = rabbit
                added_rabbits += 1
                print(
                    f"Rabbit added at ({random_row}, {random_col}) - Total: {added_rabbits}/{self.NUMBEROFRABBITS}")

    def initalizeGame(self):
        self.init_veggies()
        self.init_captain()
        self.init_Rabbits()

    def remainingVeggies(self):
        count_veggies = sum(isinstance(item, Veggie)
                            for row in self.field for item in row if item is not None)
        return count_veggies

    def intro(self):
        print("Welcome to Captain Veggie!")
        print("The rabbits have invaded your garden and you must harvest "
              "as many vegetables as possible before the rabbits eat them all!")
        print("Each vegetable is worth a different number of points, so go for the high score!\n")

        print("The vegetables are: ")
        for veg in self.possible_veggies:
            print(veg)

        print(
            f"\nCaptain Veggie is V and Rabbits are R.\n")
        print("Good luck!")

    def printField(self):
        cols = len(self.field[0])

        print("+" + "-" * cols * 3 + "+")
        for row in self.field:
            print("|", end="")
            for item in row:
                if item is None:
                    print("   ", end="")
                elif isinstance(item, FieldInhabitant):
                    print(f" {item.get_symbol()} ", end="")
                else:
                    print("???", end="")
            print("|")
        print("+" + "-" * cols * 3 + "+")

    def getScore(self):
        return self.score
