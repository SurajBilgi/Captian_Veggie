# Author: Mihir Jain, Suraj S Bilgi
# Date: 25-11-2023
# Description: A code to Create a class named Veggie to handle the Data and Functionality 

# Importing the FieldInhabitant Class
from FieldInhabitant import FieldInhabitant

# Instantiation of the Class Veggie
class Veggie(FieldInhabitant):
    def __init__(self, name, symbol, points):
        super().__init__(symbol)
        self._name = name
        self._points = points

    def __str__(self):
        return f"Symbol: {self.get_symbol()}, Name: {self._name}, Points: {self._points}"

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_points(self):
        return self._points

    def set_points(self, points):
        self._points = points
