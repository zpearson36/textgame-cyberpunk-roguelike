from game import Game

class Character(Game):

    def __init__(self, name):
        self._name = name
        self._health = 5

    def getName(self):
        return self._name

    def decrHealth(self, ammount = 1):
        self._health -= ammount

    def hit(self, target):
        target.decrHealth(2)
