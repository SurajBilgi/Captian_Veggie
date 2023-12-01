# Author: Mihir Jain, Suraj S Bilgi
# Date: 25-11-2023
# Description: A code to Create a class named Creature to handle the Data and Functionality 

# Importing the FieldInhabitant Class
from FieldInhabitant import FieldInhabitant

# Instantiation of the Class Creature
class Creature(FieldInhabitant):
    def __init__(self, x, y, symbol):
        super().__init__(symbol)
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, new_x):
        self._x = new_x

    def get_y(self):
        return self._y

    def set_y(self, new_y):
        self._y = new_y
