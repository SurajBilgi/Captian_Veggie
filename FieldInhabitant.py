# Author: Mihir Jain, Suraj S Bilgi
# Date: 25-11-2023
# Description: A code to Create a class named FieldInhabitant to handle the Data and Functionality 

# Instantiation of the Class FieldInhabitant
class FieldInhabitant:
    def __init__(self, symbol):
        self._symbol = symbol

    def get_symbol(self):
        return self._symbol

    def set_symbol(self, symbol):
        self._symbol = symbol
