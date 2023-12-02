# Author: Mihir Jain, Suraj S Bilgi
# Date: 25-11-2023
# Description: A code to Create a class named Captain to handle the Data and Functionality 

# Importing the Creature Class
from Creature import Creature

# Instantiation of the Class Captain
class Captain(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, 'V')
        self._collected_veggies = []

    def add_veggie(self, veggie):
        self._collected_veggies.append(veggie)

    def get_collected_veggies(self):
        return self._collected_veggies

    def set_collected_veggies(self, new_veggies):
        self._collected_veggies = new_veggies

    def remove5veggies(self):
        self._collected_veggies = self._collected_veggies[:-5]
