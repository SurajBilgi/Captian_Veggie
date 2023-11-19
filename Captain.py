from Creature import Creature


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
