# Mihir Jain
# Nov 20th 2023
# Game Engine For the game


# TODO - Comments and uncomment operational and Final Testing
# should rabbits move when invalid input by user?
# what if both rabbit and captain move to the same index

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

    def moveRabbits(self):
        rows = len(self.field)
        cols = len(self.field[0])
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1), (1, 0), (1, 1)]

        for rabbit in self.rabbits:
            movement_x, movement_y = random.choice(directions)
            new_x, new_y = rabbit.get_x() + movement_x, rabbit.get_y() + movement_y

            if 0 <= new_x < rows and 0 <= new_y < cols:
                new_location = self.field[new_x][new_y]
                if new_location is None or isinstance(new_location, Veggie):
                    if isinstance(new_location, Veggie):
                        self.field[new_x][new_y] = rabbit
                        self.field[rabbit.get_x()][rabbit.get_y()] = None
                        rabbit.set_x(new_x)
                        rabbit.set_y(new_y)

                    else:
                        self.field[rabbit.get_x()][rabbit.get_y()] = None
                        self.field[new_x][new_y] = rabbit
                        rabbit.set_x(new_x)
                        rabbit.set_y(new_y)

    def moveCptVertical(self, movement):
        current_x = self.captain.get_x()
        current_y = self.captain.get_y()
        new_x = current_x + movement
        rows = len(self.field)

        if 0 <= new_x < rows:
            new_location = self.field[new_x][current_y]
            if new_location is None:
                self.field[current_x][current_y] = None
                self.field[new_x][current_y] = self.captain
                self.captain.set_x(new_x)
            elif isinstance(new_location, Veggie):
                self.field[current_x][current_y] = None
                self.field[new_x][current_y] = self.captain
                self.captain.set_x(new_x)
                self.score += new_location.get_points()
                self.captain.add_veggie(new_location)
                print(f"A delicious {new_location.get_name()} found!")
            elif isinstance(new_location, Rabbit):
                print("You should not step on the rabbits")
        else:
            print("The movement is outside the boundaries. Cannot move.")

    def moveCptHorizontal(self, movement):
        current_x = self.captain.get_x()
        current_y = self.captain.get_y()
        new_y = current_y + movement
        cols = len(self.field[0])

        if 0 <= new_y < cols:
            new_location = self.field[current_x][new_y]
            if new_location is None:
                self.field[current_x][current_y] = None
                self.field[current_x][new_y] = self.captain
                self.captain.set_y(new_y)
            elif isinstance(new_location, Veggie):
                self.field[current_x][current_y] = None
                self.field[current_x][new_y] = self.captain
                self.captain.set_y(new_y)
                self.score += new_location.get_points()
                self.captain.add_veggie(new_location)
                print(f"A delicious {new_location.get_name()} found!")
            elif isinstance(new_location, Rabbit):
                print("You should not step on the rabbits.")
        else:
            print("The movement is outside the boundaries. Cannot move.")

    def moveCaptain(self):
        direction = input(
            "Enter direction to move the Captain object (Up(W), Down(S), Left(A), Right(D)): ")
        direction = direction.lower()

        if direction in ['w', 's', 'a', 'd']:
            if direction == 'w':
                self.moveCptVertical(-1)  # up
            elif direction == 's':
                self.moveCptVertical(1)  # down
            elif direction == 'a':
                self.moveCptHorizontal(-1)  # left
            elif direction == 'd':
                self.moveCptHorizontal(1)  # right
        else:
            print("Invalid input. Please enter W, A, S, or D.")

    def gameOver(self):
        print("Game Over!")
        print("The vegetables harvested:")
        for veggie in self.captain.get_collected_veggies():
            print(veggie.get_name())
        print(f"Your score: {self.score}")

    def highScore(self):
        high_scores = []
        if os.path.exists(self.HIGHSCOREFILE):
            with open(self.HIGHSCOREFILE, 'rb') as file:
                high_scores = pickle.load(file)

        initials = input("Enter your initials: ")[:3]
        player_score = (initials, self.score)

        if not high_scores:
            high_scores.append(player_score)
        else:
            for i, (initial, score) in enumerate(high_scores):
                if player_score[1] > score:
                    high_scores.insert(i, player_score)
                    break
            else:
                high_scores.append(player_score)

        print("High Scores:")
        for idx, (initial, score) in enumerate(high_scores, start=1):
            print(f"{idx}. {initial}: {score}")

        with open(self.HIGHSCOREFILE, 'wb') as file:
            pickle.dump(high_scores, file)