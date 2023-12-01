# Author: Mihir Jain, Suraj S Bilgi
# Date: 25-11-2023
# Description: A code to Create a class named Rabbit to handle the Data and Functionality 

# Importing the Creature Class
from Creature import Creature

# Instantiation of the Class Rabbit
class Rabbit(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, 'R')
